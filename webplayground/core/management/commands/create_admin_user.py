import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crea un usuario administrador automáticamente'

    def handle(self, *args, **options):
        # Credenciales del admin (puedes cambiarlas o usar variables de entorno)
        admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
        admin_email = os.environ.get('ADMIN_EMAIL', 'admin@webplayground.com')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123456')

        # Verificar si el usuario admin ya existe
        if User.objects.filter(username=admin_username).exists():
            self.stdout.write(
                self.style.WARNING(f'El usuario admin "{admin_username}" ya existe.')
            )
            return

        # Crear el superusuario
        try:
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Usuario admin "{admin_username}" creado exitosamente.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error al crear el usuario admin: {e}')
            )
