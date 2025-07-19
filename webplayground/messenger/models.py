from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError

# Create your models here.

class ThreadManager(models.Manager):
    def find(self, user1, user2):
        # Filtrar por ambos usuarios usando Q objects
        queryset = self.filter(
            Q(users=user1) & Q(users=user2)
        ).distinct()
        
        # Si encontramos exactamente 1 hilo, lo devolvemos
        if queryset.count() == 1:
            return queryset.first()
        # Si no encontramos ninguno o hay más de uno, devolvemos None
        return None
    
    def find_or_create(self, user1, user2):
        # Intentar encontrar el hilo existente
        thread = self.find(user1, user2)
        
        # Si no existe, crear uno nuevo
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
            
        return thread

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    updated = models.DateTimeField(auto_now=True)
    
    objects = ThreadManager()
    
    class Meta:
        ordering = ['-updated']
        
    def __str__(self):
        if self.users.count() == 2:
            users = list(self.users.all())
            return f"Conversación entre {users[0].username} y {users[1].username}"
        return f"Conversación {self.pk}"

class MessageManager(models.Manager):
    def create(self, **kwargs):
        # Validar que el usuario esté en el hilo antes de crear el mensaje
        user = kwargs.get('user')
        thread = kwargs.get('thread')
        
        if user and thread and user not in thread.users.all():
            print(f"¡Usuario {user.username} no pertenece al hilo!")
            # En lugar de crear el mensaje, retornamos None o lanzamos una excepción
            # Para TDD, simplemente no creamos el mensaje
            return None
        
        # Si todo está bien, crear el mensaje normalmente
        return super().create(**kwargs)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    objects = MessageManager()
    
    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return f"Mensaje de {self.user.username} en {self.thread}"
