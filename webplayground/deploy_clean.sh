#!/bin/bash

# Script de deploy limpio para Render
echo "🚀 Iniciando WebPlayground Deploy..."

echo "🔍 Verificando ubicación actual:"
pwd
ls -la

echo "🔍 Verificando configuración de base de datos..."
python manage.py shell -c "
from django.conf import settings
print('ENGINE:', settings.DATABASES['default']['ENGINE'])
print('NAME:', settings.DATABASES['default']['NAME'])
print('USER:', settings.DATABASES['default'].get('USER', ''))
print('HOST:', settings.DATABASES['default'].get('HOST', ''))
print('PORT:', settings.DATABASES['default'].get('PORT', ''))
"

echo "🗄️ Ejecutando migraciones..."
python manage.py migrate --noinput --verbosity=2

echo "📦 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput --verbosity=2

echo "🚀 Iniciando Gunicorn..."
exec gunicorn webplayground.wsgi:application --bind 0.0.0.0:$PORT --log-file - --access-logfile - --error-logfile -
