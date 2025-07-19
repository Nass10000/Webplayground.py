from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import os

def custom_upload_to(instance, filename):
    # Obtener el avatar antiguo si existe
    old_instance = Profile.objects.filter(pk=instance.pk).first()
    if old_instance and old_instance.avatar:
        # Usar el método delete() del campo ImageField
        old_instance.avatar.delete()
    
    # Devolver la nueva ruta
    return f'profiles/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        
    def __str__(self):
        return f"Perfil de {self.user.username}"

# Señal para eliminar el avatar anterior antes de guardar uno nuevo
@receiver(pre_save, sender=Profile)
def delete_old_avatar(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Profile.objects.get(pk=instance.pk)
            if old_instance.avatar and old_instance.avatar != instance.avatar:
                old_instance.avatar.delete(save=False)
        except Profile.DoesNotExist:
            pass

# Señal para crear automáticamente el perfil cuando se crea un usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # print(f"Creando perfil de {instance.username}")  # Comentado para tests

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
