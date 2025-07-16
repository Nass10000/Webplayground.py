import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webplayground.settings')
django.setup()

from pages.models import Page

# Crear páginas de prueba
pages_data = [
    {
        'title': 'Etiam pharetra risus eu venenatis sodales',
        'content': '''Etiam pharetra risus eu venenatis sodales. Donec ut arcu rhoncus odio quis malesuada felis. Aenean non lacus tamen. Nullam ac neque tortor dignissim. Praesent ut tellus ligula elit tempor id. Duis malesuada commodo mauris at arcu cursus. Sed id mauris quis ante congue bibendum. Sed luctus elit in ligula rhoncus molestie et id leo. Nunc tempor massa at mauris consectetur at rhoncus lorem luctus. Sed luctus augue risus et blandit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.'''
    },
    {
        'title': 'Lorem ipsum dolor sit amet',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed facilisis lorem non tempor sagittis a finibus magna commodo et. Mauris ac ante tellus. Quisque non dui vitae elit dignissim vehiculum nec et lorem.'''
    }
]

# Eliminar páginas existentes y crear nuevas
Page.objects.all().delete()

for page_data in pages_data:
    page = Page.objects.create(**page_data)
    print(f"Página creada: {page.title}")

print("Páginas de prueba creadas exitosamente!")
