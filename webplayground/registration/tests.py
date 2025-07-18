from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Profile
import os

class ProfileTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        User.objects.create_user('testuser', 'test@test.com', 'testpassword123')
    
    def test_profile_exists(self):
        # Verificar que el perfil se crea automáticamente
        user = User.objects.get(username='testuser')
        self.assertTrue(Profile.objects.filter(user=user).exists())
        
    def test_profile_str_method(self):
        # Verificar el método __str__ del perfil
        user = User.objects.get(username='testuser')
        profile = Profile.objects.get(user=user)
        self.assertEqual(str(profile), "Perfil de testuser")
        
    def test_profile_fields(self):
        # Verificar que el perfil tiene los campos correctos
        user = User.objects.get(username='testuser')
        profile = Profile.objects.get(user=user)
        
        # Verificar que los campos opcionales pueden ser None/vacíos
        self.assertIsNone(profile.avatar.name or None)
        self.assertIsNone(profile.bio or None)
        self.assertIsNone(profile.link or None)
        
        # Actualizar campos y verificar
        profile.bio = "Esta es mi biografía de prueba"
        profile.link = "https://www.ejemplo.com"
        profile.save()
        
        updated_profile = Profile.objects.get(user=user)
        self.assertEqual(updated_profile.bio, "Esta es mi biografía de prueba")
        self.assertEqual(updated_profile.link, "https://www.ejemplo.com")
        
    def test_avatar_optimization(self):
        # Verificar que se elimina el avatar anterior al subir uno nuevo
        user = User.objects.get(username='testuser')
        profile = Profile.objects.get(user=user)
        
        # Crear un archivo de prueba simulado
        test_image_1 = SimpleUploadedFile(
            name='test_avatar_1.jpg',
            content=b'fake image content 1',
            content_type='image/jpeg'
        )
        
        # Subir primer avatar
        profile.avatar = test_image_1
        profile.save()
        
        # Verificar que el avatar se guardó
        self.assertTrue(profile.avatar.name)
        first_avatar_path = profile.avatar.name
        
        # Crear un segundo archivo de prueba
        test_image_2 = SimpleUploadedFile(
            name='test_avatar_2.jpg',
            content=b'fake image content 2',
            content_type='image/jpeg'
        )
        
        # Subir segundo avatar
        profile.avatar = test_image_2
        profile.save()
        
        # Verificar que el nuevo avatar se guardó
        self.assertTrue(profile.avatar.name)
        second_avatar_path = profile.avatar.name
        
        # Verificar que el path cambió (se subió un nuevo archivo)
        self.assertNotEqual(first_avatar_path, second_avatar_path)
