#!/usr/bin/env python
"""
Script de emergencia para crear admin
Copia este código y pégalo en la consola de Render (Python shell)
"""

# Para ejecutar en Render shell:
# 1. Ve a tu servicio en Render
# 2. Click en "Shell" 
# 3. Copia y pega el siguiente código:

from django.contrib.auth.models import User

# Eliminar cualquier admin existente
User.objects.filter(username='admin').delete()

# Crear nuevo admin
admin = User.objects.create_superuser(
    username='admin',
    email='admin@webplayground.com', 
    password='admin123'
)

print("✅ Admin creado exitosamente!")
print("Username: admin")
print("Password: admin123")
print("Email: admin@webplayground.com")
