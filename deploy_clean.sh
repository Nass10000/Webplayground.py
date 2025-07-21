#!/bin/bash
echo "🔍 Verificando configuración de base de datos..."
python manage.py shell -c "
from django.conf import settings
import os
print('='*50)
print('CONFIGURACIÓN DE BASE DE DATOS:')
print('='*50)
print(f'DATABASE_URL en env: {\"DATABASE_URL\" in os.environ}')
if 'DATABASE_URL' in os.environ:
    print(f'DATABASE_URL: {os.environ.get(\"DATABASE_URL\")[:50]}...')
print(f'Engine: {settings.DATABASES[\"default\"][\"ENGINE\"]}')
print(f'Name: {settings.DATABASES[\"default\"][\"NAME\"]}')
print(f'User: {settings.DATABASES[\"default\"].get(\"USER\", \"N/A\")}')
print(f'Host: {settings.DATABASES[\"default\"].get(\"HOST\", \"N/A\")}')
print(f'Port: {settings.DATABASES[\"default\"].get(\"PORT\", \"N/A\")}')
print('='*50)
"

echo "🗄️ Ejecutando migraciones..."
python manage.py migrate --noinput --verbosity=2

echo "📦 Recopilando archivos estáticos..."cript de deploy limpio para Render
echo "🚀 Iniciando WebPlayground Deploy..."

# Navegar al directorio del proyecto Django
cd webplayground

echo "🔍 Verificando ubicación actual:"
pwd
ls -la

echo "🗄️ Ejecutando migraciones..."
python manage.py migrate --noinput --verbosity=2

echo "� Recopilando archivos estáticos..."
python manage.py collectstatic --noinput --verbosity=2

echo "🚀 Iniciando Gunicorn..."
exec gunicorn webplayground.wsgi:application --bind 0.0.0.0:$PORT --log-file - --access-logfile - --error-logfile -
