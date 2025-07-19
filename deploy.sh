#!/bin/bash

# Script de despliegue para Web Playground
echo "🚀 Iniciando proceso de despliegue..."

# Crear entorno virtual (si no existe)
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python -m venv venv
fi

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
