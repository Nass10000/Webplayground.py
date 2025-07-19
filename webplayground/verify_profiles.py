import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webplayground.settings')
django.setup()

from django.contrib.auth.models import User
from registration.models import Profile

print("=== Verificación de Usuarios y Perfiles ===\n")

# Verificar todos los usuarios
users = User.objects.all()
print(f"Total de usuarios: {users.count()}")

for user in users:
    print(f"\n👤 Usuario: {user.username}")
    print(f"   Email: {user.email}")
    print(f"   Fecha de registro: {user.date_joined}")
    
    try:
        profile = user.profile
        print(f"   ✅ Tiene perfil: Sí")
        print(f"   Bio: {profile.bio[:50] if profile.bio else 'Sin biografía'}...")
        print(f"   Link: {profile.link or 'Sin enlace'}")
        print(f"   Avatar: {'Sí' if profile.avatar else 'No'}")
    except Profile.DoesNotExist:
        print(f"   ❌ Tiene perfil: No")

print(f"\n=== Resumen ===")
profiles_count = Profile.objects.count()
print(f"Total de perfiles: {profiles_count}")

if profiles_count > 0:
    print("✅ Los perfiles deberían mostrarse en /profiles/")
else:
    print("❌ No hay perfiles para mostrar")
