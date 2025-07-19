import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webplayground.settings')
django.setup()

from django.contrib.auth.models import User
from registration.models import Profile

# Datos de usuarios adicionales para probar paginación
additional_users_data = [
    {
        'username': 'elena_santos',
        'email': 'elena@example.com',
        'password': 'test123456',
        'bio': 'Especialista en seguridad informática y ciberseguridad. Apasionada por proteger sistemas y datos.',
        'link': 'https://elena-security.com'
    },
    {
        'username': 'miguel_torres',
        'email': 'miguel@example.com',
        'password': 'test123456',
        'bio': 'DevOps Engineer con experiencia en AWS y Docker. Me gusta automatizar procesos y optimizar infraestructuras.',
        'link': 'https://miguel-devops.com'
    },
    {
        'username': 'sofia_mendez',
        'email': 'sofia@example.com',
        'password': 'test123456',
        'bio': 'Product Manager en tecnología. Conectando las necesidades del usuario con soluciones técnicas innovadoras.',
        'link': 'https://linkedin.com/in/sofia-mendez'
    },
    {
        'username': 'alejandro_kim',
        'email': 'alejandro@example.com',
        'password': 'test123456',
        'bio': 'Mobile Developer especializado en React Native y Flutter. Creando apps que transforman vidas.',
        'link': 'https://alejandro-apps.com'
    },
    {
        'username': 'lucia_fernandez',
        'email': 'lucia@example.com',
        'password': 'test123456',
        'bio': 'QA Engineer y testing automation expert. Garantizando la calidad en cada línea de código.',
        'link': 'https://lucia-qa.com'
    }
]

print("Creando usuarios adicionales para probar paginación...")

for user_data in additional_users_data:
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

total_users = User.objects.filter(profile__isnull=False).count()
print(f"\n🎉 Proceso completado!")
print(f"📊 Total de usuarios con perfil: {total_users}")
print(f"📄 Con paginación de 3 por página, tendremos {(total_users + 2) // 3} páginas")

print("\n🔍 Ahora puedes probar la paginación en /profiles/")
print("   - Página 1: /profiles/")
print("   - Página 2: /profiles/?page=2")
print("   - Página 3: /profiles/?page=3")
