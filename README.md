# Webplayground

Esta página desplegada en WebPlayground-PY ([https://webplayground-py.onrender.com](https://webplayground-py.onrender.com)) muestra una aplicación Python/Django robusta con autenticación, administración de contenidos, bases de datos PostgreSQL y diseño responsivo. Explora funcionalidades interactivas y prácticas de seguridad.

Proyecto web desarrollado con **Django 5.2.4** y desplegado en **Render** usando **PostgreSQL** como base de datos principal.

## Características principales
- Autenticación de usuarios (admin y usuarios normales)
- Panel de administración de Django
- Gestión de páginas y perfiles
- Editor CKEditor integrado
- Sistema de mensajería interna
- Archivos estáticos servidos con WhiteNoise
- Configuración segura para producción

## Estructura del proyecto
```
webplayground/
├── core/                # App principal
├── pages/               # App de páginas
├── profiles/            # App de perfiles
├── messenger/           # App de mensajería
├── registration/        # App de registro de usuarios
├── webplayground/       # Configuración global y settings.py
│   ├── settings.py      # Configuración de Django y base de datos
│   ├── urls.py          # URLs principales
│   └── wsgi.py          # WSGI para producción
├── requirements.txt     # Dependencias del proyecto
└── manage.py            # Comando principal de Django
```

## Instalación local
1. Clona el repositorio:
   ```bash
   git clone <repo-url>
   cd Webplayground.py
   ```
2. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Crea el archivo `.env` con tus variables:
   ```env
   SECRET_KEY=tu_clave_secreta
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   EMAIL_FILE_PATH=sent_emails
   ```
4. Aplica migraciones y ejecuta el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Despliegue en Render
- El proyecto está preparado para desplegarse en [Render](https://render.com/)
- Usa PostgreSQL como base de datos persistente
- Variables de entorno necesarias en Render:
  - `DATABASE_URL` (proporcionada por Render)
  - `SECRET_KEY`
  - `DEBUG` (False en producción)
  - `ALLOWED_HOSTS` (tu dominio de Render)

### Comando de inicio recomendado en Render
```
cd webplayground && echo "🔍 Verificando configuración de base de datos..." && python manage.py shell -c "from django.conf import settings; print('ENGINE:', settings.DATABASES['default']['ENGINE']); print('NAME:', settings.DATABASES['default']['NAME']); print('USER:', settings.DATABASES['default'].get('USER', '')); print('HOST:', settings.DATABASES['default'].get('HOST', '')); print('PORT:', settings.DATABASES['default'].get('PORT', ''))" && echo "✅ Iniciando aplicación..." && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn webplayground.wsgi:application --bind 0.0.0.0:$PORT
```

## Usuarios de prueba
- **Admin:**
  - Usuario: `admin`
  - Email: `admin@webplayground.com`
  - Contraseña: `admin123`
- **Usuario normal:**
  - Usuario: `Liza100`
  - Email: `liza@webplayground.com`
  - Contraseña: `eli2345!`

## Acceso al panel de administración
- URL: `/admin/`
- Accede con el usuario admin

## Notas técnicas
- Usa `psycopg[binary]` para compatibilidad con Python 3.13
- El settings.py detecta automáticamente si usar PostgreSQL (Render) o SQLite (local)
- Los archivos estáticos se sirven con WhiteNoise
- El proyecto está preparado para producción y desarrollo

---

**Desarrollado por Nass10000**
