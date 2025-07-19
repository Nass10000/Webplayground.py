from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.

class ThreadTestCase(TestCase):
    def setUp(self):
        # Crear usuarios de prueba
        self.user1 = User.objects.create_user('user1', 'user1@test.com', 'test123456')
        self.user2 = User.objects.create_user('user2', 'user2@test.com', 'test123456')
        self.user3 = User.objects.create_user('user3', 'user3@test.com', 'test123456')
        
        # Crear un hilo de conversación
        self.thread = Thread.objects.create()
        
    def test_add_users_to_thread(self):
        # Añadir usuarios al hilo
        self.thread.users.add(self.user1, self.user2)
        
        # Verificar que el hilo tiene exactamente 2 usuarios
        self.assertEqual(self.thread.users.count(), 2)
        
    def test_filter_thread_by_users(self):
        # Añadir usuarios al hilo
        self.thread.users.add(self.user1, self.user2)
        
        # Recuperar el hilo filtrando por los dos usuarios
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        
        # Verificar que encontramos exactamente 1 hilo y es el correcto
        self.assertEqual(threads.count(), 1)
        self.assertEqual(threads.first(), self.thread)
        
    def test_filter_non_existent_thread(self):
        # Añadir usuarios al hilo (user1 y user2)
        self.thread.users.add(self.user1, self.user2)
        
        # Intentar recuperar un hilo con user1 y user3 (que no existe)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user3)
        
        # Verificar que no se encuentra ningún hilo
        self.assertEqual(threads.count(), 0)
        
    def test_add_messages_to_thread(self):
        # Añadir usuarios al hilo
        self.thread.users.add(self.user1, self.user2)
        
        # Crear algunos mensajes
        message1 = Message.objects.create(user=self.user1, thread=self.thread, content="Hola, ¿cómo estás?")
        message2 = Message.objects.create(user=self.user2, thread=self.thread, content="¡Hola! Muy bien, ¿y tú?")
        message3 = Message.objects.create(user=self.user1, thread=self.thread, content="Genial, gracias por preguntar")
        
        # Verificar que el hilo tiene exactamente 3 mensajes
        self.assertEqual(self.thread.messages.count(), 3)
        
        # Verificar que los mensajes están en el orden correcto (por fecha de creación)
        messages = self.thread.messages.all()
        self.assertEqual(messages[0], message1)
        self.assertEqual(messages[1], message2)
        self.assertEqual(messages[2], message3)
        
        # Mostrar la conversación (para debug)
        print("\n--- Conversación ---")
        for message in messages:
            print(f"{message.user.username}: {message.content}")
        print("--- Fin conversación ---\n")
        
    def test_add_message_from_user_not_in_thread(self):
        # Añadir usuarios al hilo (user1 y user2)
        self.thread.users.add(self.user1, self.user2)
        
        # Crear mensajes válidos de usuarios en el hilo
        message1 = Message.objects.create(user=self.user1, thread=self.thread, content="Hola, ¿cómo estás?")
        message2 = Message.objects.create(user=self.user2, thread=self.thread, content="¡Hola! Muy bien, ¿y tú?")
        
        # Intentar crear un mensaje desde user3 que NO está en el hilo
        # Esto debería retornar None debido a la validación en el Manager
        message3 = Message.objects.create(user=self.user3, thread=self.thread, content="Mensaje intruso")
        
        # Verificar que el mensaje fraudulento no se creó
        self.assertIsNone(message3)
        
        # El hilo debería tener solo 2 mensajes (excluyendo el del user3)
        self.assertEqual(self.thread.messages.count(), 2)
        
    def test_find_thread_with_custom_manager(self):
        # Añadir usuarios al hilo
        self.thread.users.add(self.user1, self.user2)
        
        # Buscar el hilo usando el manager personalizado
        thread = Thread.objects.find(self.user1, self.user2)
        
        # Verificar que encontramos el hilo correcto
        self.assertEqual(thread, self.thread)
        
    def test_find_thread_that_does_not_exist(self):
        # Añadir usuarios al hilo (user1 y user2)
        self.thread.users.add(self.user1, self.user2)
        
        # Buscar un hilo que no existe (user1 y user3)
        thread = Thread.objects.find(self.user1, self.user3)
        
        # Verificar que retorna None
        self.assertIsNone(thread)
        
    def test_find_or_create_existing_thread(self):
        # Añadir usuarios al hilo existente
        self.thread.users.add(self.user1, self.user2)
        
        # Intentar buscar o crear el mismo hilo
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        
        # Debería devolver el hilo existente
        self.assertEqual(thread, self.thread)
        
        # Verificar que no se creó un nuevo hilo
        self.assertEqual(Thread.objects.count(), 1)
        
    def test_find_or_create_new_thread(self):
        # Añadir usuarios al hilo existente (user1 y user2)
        self.thread.users.add(self.user1, self.user2)
        
        # Buscar o crear un hilo nuevo (user1 y user3)
        new_thread = Thread.objects.find_or_create(self.user1, self.user3)
        
        # Verificar que se creó un nuevo hilo
        self.assertNotEqual(new_thread, self.thread)
        self.assertEqual(Thread.objects.count(), 2)
        
        # Verificar que el nuevo hilo tiene los usuarios correctos
        self.assertIn(self.user1, new_thread.users.all())
        self.assertIn(self.user3, new_thread.users.all())
        self.assertEqual(new_thread.users.count(), 2)
