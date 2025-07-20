from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import os

class Command(BaseCommand):
    help = 'Force create all database tables for Render deployment'

    def handle(self, *args, **options):
        self.stdout.write('🔍 Checking database connection...')
        
        # Verificar conexión a la base de datos
        try:
            connection.ensure_connection()
            self.stdout.write(self.style.SUCCESS('✅ Database connection successful'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Database connection failed: {e}'))
            return
        
        # Crear base de datos si no existe
        self.stdout.write('🗄️  Creating database tables...')
        
        # Ejecutar migraciones
        self.stdout.write('📋 Running migrations...')
        call_command('migrate', verbosity=2, interactive=False)
        
        # Verificar que las tablas existan
        self.stdout.write('🔍 Checking if tables exist...')
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
        self.stdout.write(f'📊 Found {len(tables)} tables in database:')
        for table in tables:
            self.stdout.write(f'  - {table[0]}')
        
        # Recopilar archivos estáticos
        self.stdout.write('📦 Collecting static files...')
        call_command('collectstatic', verbosity=1, interactive=False)
        
        self.stdout.write(self.style.SUCCESS('🎉 Database setup completed successfully!'))
