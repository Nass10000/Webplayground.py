#!/bin/bashecho "🔧 Ejecutando configuración forzada de base de datos..."
python manage.py force_setupdespliegue para Web Playground - Render
echo "🚀 Iniciando despliegue de WebPlayground en Render..."

# Cambiar al directorio correcto
cd webplayground

echo "📋 Verificando estructura del proyecto..."
ls -la

echo "🔍 Verificando migraciones disponibles..."
python manage.py showmigrations

echo "🗄️  Ejecutando migraciones..."
python manage.py migrate --verbosity=2

echo "🗄️  Verificando estado después de migraciones..."
python manage.py showmigrations

echo "📦 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput --verbosity=2

echo "� Verificando configuración de la aplicación..."
python manage.py check

echo "🚀 Iniciando servidor Gunicorn..."
exec gunicorn webplayground.wsgi:application --log-file - --bind 0.0.0.0:$PORT --access-logfile - --error-logfile -

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

# Navegar al directorio del proyecto
cd webplayground

# Ejecutar migraciones
echo "🗄️ Ejecutando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Recopilar archivos estáticos
echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# Crear superusuario (opcional)
echo "👤 ¿Quieres crear un superusuario? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py createsuperuser
fi

echo "✅ ¡Despliegue completado!"
echo "🌐 Para ejecutar el servidor: python manage.py runserver"
