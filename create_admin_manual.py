#!/usr/bin/env python
"""
Script manual para crear usuario admin en producción
Ejecutar este script en el shell de Render si las credenciales no funcionan
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webplayground.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    username = 'admin'
    email = 'admin@webplayground.com'
    password = 'demo123'
    
    # Eliminar usuario existente si existe
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.delete()
        print(f'Usuario existente "{username}" eliminado')
    
    # Crear nuevo admin
    User.objects.create_superuser(username, email, password)
    print(f'Superuser "{username}" creado exitosamente!')
    print(f'Username: {username}')
    print(f'Password: {password}')
    print(f'Email: {email}')

if __name__ == '__main__':
    create_admin()
