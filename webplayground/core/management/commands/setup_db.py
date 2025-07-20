from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Setup database for production deployment'

    def handle(self, *args, **options):
        self.stdout.write('Setting up database...')
        
        # Ejecutar migraciones
        self.stdout.write('Running migrations...')
        call_command('migrate', verbosity=2, interactive=False)
        
        # Recopilar archivos estáticos
        self.stdout.write('Collecting static files...')
        call_command('collectstatic', verbosity=2, interactive=False)
        
        self.stdout.write(self.style.SUCCESS('Database setup completed successfully!'))
