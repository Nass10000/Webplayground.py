import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webplayground.settings')
django.setup()

from django.contrib.auth.models import User
from registration.models import Profile

# Datos de usuarios de prueba
users_data = [
    {
        'username': 'maria_garcia',
        'email': 'maria@example.com',
        'password': 'test123456',
        'bio': 'Desarrolladora web apasionada por Django y Python. Me encanta crear aplicaciones innovadoras y colaborar en proyectos open source.',
        'link': 'https://github.com/maria-garcia'
    },
    {
        'username': 'carlos_lopez',
        'email': 'carlos@example.com',
        'password': 'test123456',
        'bio': 'Diseñador UX/UI con experiencia en desarrollo frontend. Siempre buscando crear interfaces intuitivas y atractivas.',
        'link': 'https://portfolio-carlos.com'
    },
    {
        'username': 'ana_martinez',
        'email': 'ana@example.com',
        'password': 'test123456',
        'bio': 'Data Scientist y entusiasta del machine learning. Me gusta convertir datos en insights útiles para las empresas.',
        'link': 'https://linkedin.com/in/ana-martinez'
    },
    {
        'username': 'david_ruiz',
        'email': 'david@example.com',
        'password': 'test123456',
        'bio': 'Full-stack developer especializado en Django y React. Cofundador de una startup tecnológica.',
        'link': 'https://david-dev.com'
    }
]

print("Creando usuarios de prueba...")

for user_data in users_data:
    # Verificar si el usuario ya existe
    if not User.objects.filter(username=user_data['username']).exists():
        # Crear usuario
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        
        # Actualizar perfil (se crea automáticamente con la señal)
        profile = user.profile
        profile.bio = user_data['bio']
        profile.link = user_data['link']
        profile.save()
        
        print(f"✅ Usuario creado: {user.username}")
    else:
        print(f"⚠️  Usuario ya existe: {user_data['username']}")

print("\n🎉 Proceso completado!")
print("\nUsuarios de prueba creados:")
for user_data in users_data:
    print(f"- {user_data['username']} | {user_data['email']} | Password: {user_data['password']}")

print("\n📝 Puedes usar estos usuarios para probar la funcionalidad de perfiles públicos.")
