# 🚀 Guía de Despliegue - Web Playground

Esta guía te ayudará a desplegar tu aplicación Web Playground en diferentes entornos.

## 📋 Preparación del Proyecto

### 1. Variables de Entorno
Copia el archivo `.env.example` como `.env` y configura las variables:

```bash
cp .env.example .env
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar Base de Datos
```bash
cd webplayground
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear Superusuario
```bash
python manage.py createsuperuser
```

### 5. Recopilar Archivos Estáticos
```bash
python manage.py collectstatic
```

## 🌐 Despliegue en Heroku

### Preparación
1. Instala Heroku CLI
2. Inicia sesión: `heroku login`

### Despliegue
```bash
# Crear aplicación en Heroku
heroku create tu-app-name

# Configurar variables de entorno
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=tu-nueva-clave-secreta-segura
heroku config:set ALLOWED_HOSTS=tu-app-name.herokuapp.com

# Para producción con SSL
heroku config:set SECURE_SSL_REDIRECT=True
heroku config:set SESSION_COOKIE_SECURE=True
heroku config:set CSRF_COOKIE_SECURE=True
heroku config:set SECURE_HSTS_SECONDS=31536000
heroku config:set SECURE_HSTS_INCLUDE_SUBDOMAINS=True
heroku config:set SECURE_HSTS_PRELOAD=True

# Desplegar
git push heroku main

# Ejecutar migraciones en Heroku
heroku run python webplayground/manage.py migrate

# Crear superusuario en Heroku
heroku run python webplayground/manage.py createsuperuser
```

## 🐧 Despliegue en Servidor Linux (Ubuntu)

### 1. Preparar el Servidor
```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib
```

### 2. Configurar Proyecto
```bash
# Clonar repositorio
git clone https://github.com/Nass10000/Webplayground.py.git
cd Webplayground.py

# Ejecutar script de despliegue
./deploy.sh
```

### 3. Configurar Nginx
Crear archivo `/etc/nginx/sites-available/webplayground`:

```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /path/to/your/project/webplayground;
    }
    
    location /media/ {
        root /path/to/your/project/webplayground;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/project/webplayground/webplayground.sock;
    }
}
```

### 4. Configurar Gunicorn
```bash
# Crear servicio systemd
sudo nano /etc/systemd/system/gunicorn.service
```

```ini
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=tu-usuario
Group=www-data
WorkingDirectory=/path/to/your/project/webplayground
ExecStart=/path/to/your/project/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/path/to/your/project/webplayground/webplayground.sock \
          webplayground.wsgi:application

[Install]
WantedBy=multi-user.target
```

## 🐳 Despliegue con Docker

### Dockerfile
```dockerfile
FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/webplayground

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "webplayground.wsgi:application"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=tu-clave-secreta
      - ALLOWED_HOSTS=localhost,127.0.0.1
    volumes:
      - ./webplayground/media:/app/webplayground/media
      - ./webplayground/staticfiles:/app/webplayground/staticfiles
```

## ⚙️ Variables de Entorno para Producción

```bash
# Configuraciones básicas
DEBUG=False
SECRET_KEY=clave-super-secreta-y-larga-para-produccion
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com

# Configuraciones de seguridad
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

## 🔒 Lista de Verificación de Seguridad

- [ ] DEBUG=False en producción
- [ ] SECRET_KEY única y secreta
- [ ] ALLOWED_HOSTS configurado correctamente
- [ ] HTTPS habilitado
- [ ] Configuraciones de seguridad activadas
- [ ] Base de datos segura (no SQLite en producción)
- [ ] Archivos estáticos servidos por servidor web
- [ ] Copias de seguridad configuradas

## 🆘 Solución de Problemas

### Error 500
- Verificar logs del servidor
- Comprobar configuración de DEBUG y ALLOWED_HOSTS
- Verificar que todas las variables de entorno estén configuradas

### Archivos estáticos no cargan
- Ejecutar `python manage.py collectstatic`
- Verificar configuración de STATIC_ROOT y STATIC_URL
- Comprobar configuración del servidor web

### Error de base de datos
- Verificar migraciones: `python manage.py migrate`
- Comprobar configuración de base de datos
- Verificar permisos de base de datos

---

¡Tu aplicación Web Playground está lista para producción! 🎉
