from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create superuser for production deployment'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@webplayground.com'
        password = 'admin123'
        
        # Eliminar usuario existente si existe
        if User.objects.filter(username=username).exists():
            User.objects.filter(username=username).delete()
            self.stdout.write(
                self.style.WARNING(f'Superuser "{username}" existente eliminado')
            )
        
        # Crear nuevo superuser
        User.objects.create_superuser(username, email, password)
        self.stdout.write(
            self.style.SUCCESS(f'Superuser "{username}" created successfully!')
        )
            self.stdout.write(
                self.style.SUCCESS(f'Username: {username}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'Password: {password}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'Email: {email}')
            )
