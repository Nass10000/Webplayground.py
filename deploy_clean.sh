#!/bin/bash

# Script de deploy limpio para Render
echo "🚀 Iniciando WebPlayground Deploy..."

# Navegar al directorio del proyecto Django
cd webplayground

echo "🔍 Verificando ubicación actual:"
pwd
ls -la

echo "🗄️ Ejecutando migraciones..."
python manage.py migrate --noinput --verbosity=2

echo "👤 Creando superusuario admin..."
python manage.py create_admin_user

echo "📦 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput --verbosity=2

echo "🚀 Iniciando Gunicorn..."
exec gunicorn webplayground.wsgi:application --bind 0.0.0.0:$PORT --log-file - --access-logfile - --error-logfile -
