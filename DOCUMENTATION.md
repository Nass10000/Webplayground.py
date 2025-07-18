# Django Web Playground - Documentación

## Resumen del Proyecto

Este proyecto implementa un sistema web completo en Django con las siguientes características:

### 1. Sistema de Páginas (CRUD)
- **App**: `pages`
- **Modelo**: `Page` con título, contenido (CKEditor), orden y fecha
- **Vistas**: Implementadas con Class-Based Views (CBV)
  - `ListView`: Listado de páginas
  - `DetailView`: Detalle de página individual
  - `CreateView`: Crear nueva página (solo staff)
  - `UpdateView`: Editar página (solo staff)
  - `DeleteView`: Eliminar página (solo staff)

### 2. Sistema de Autenticación
- **App**: `registration`
- **Características**:
  - Registro de usuarios con validación de email
  - Login/Logout
  - Reseteo de contraseña por email
  - Perfiles de usuario con avatar, biografía y enlace web

### 3. Configuración de Seguridad
- Acceso restringido a staff para operaciones CRUD
- Decoradores `@staff_member_required` y `@login_required`
- Mixins para control de acceso en CBV

### 4. Templates y UI
- **Bootstrap 5.1.3** para diseño responsivo
- **CKEditor** para edición de contenido enriquecido
- Templates personalizados para cada vista
- Navegación con dropdown de usuario

## Estructura del Proyecto

```
webplayground/
├── core/                  # App principal
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── sample.html
│   └── views.py
├── pages/                 # App de páginas
│   ├── models.py         # Modelo Page
│   ├── views.py          # CBV para CRUD
│   ├── urls.py           # URLs con decoradores
│   └── templates/
│       └── pages/
│           ├── page_list.html
│           └── page_detail.html
├── registration/          # App de usuarios
│   ├── models.py         # Modelo Profile
│   ├── views.py          # SignUpView, ProfileView
│   ├── forms.py          # SignUpForm, ProfileForm
│   ├── urls.py           # URLs de auth
│   ├── templates/
│   │   └── registration/
│   │       ├── signup.html
│   │       ├── login.html
│   │       ├── profile.html
│   │       └── profile_form.html
│   └── static/
│       └── registration/
│           └── img/
│               └── no-avatar.svg
└── webplayground/         # Configuración
    ├── settings.py       # Configuración completa
    └── urls.py           # URLs principales
```

## Características Implementadas

### ✅ CRUD Completo
- Crear, leer, actualizar y eliminar páginas
- Validación de permisos (solo staff)
- Formularios con CKEditor

### ✅ Sistema de Usuarios
- Registro con validación de email único
- Login/logout funcional
- Reseteo de contraseña por email
- Perfiles con avatar, biografía y enlace web

### ✅ Seguridad
- Decoradores de acceso
- Mixins para CBV
- Validación de permisos

### ✅ UI/UX
- Bootstrap 5.1.3 responsivo
- CKEditor para contenido rico
- Templates personalizados
- Navegación intuitiva

## Comandos Útiles

```bash
# Iniciar servidor
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recolectar archivos estáticos
python manage.py collectstatic
```

## URLs Disponibles

- `/` - Página de inicio
- `/pages/` - Lista de páginas
- `/pages/<id>/` - Detalle de página
- `/pages/create/` - Crear página (staff)
- `/pages/update/<id>/` - Editar página (staff)
- `/pages/delete/<id>/` - Eliminar página (staff)
- `/accounts/signup/` - Registro
- `/accounts/login/` - Login
- `/accounts/logout/` - Logout
- `/accounts/profile/` - Perfil de usuario
- `/accounts/profile/edit/` - Editar perfil

## Tecnologías Utilizadas

- **Django 5.2.4**
- **Python 3.13**
- **Bootstrap 5.1.3**
- **CKEditor**
- **SQLite**
- **Pillow** (para manejo de imágenes)

## Estado del Proyecto

El proyecto está completamente funcional con todas las características implementadas según las especificaciones del tutorial. El sistema permite:

1. Gestión completa de páginas con permisos
2. Registro y autenticación de usuarios
3. Perfiles de usuario con personalización
4. UI moderna y responsiva
5. Seguridad implementada correctamente

¡El sistema está listo para usar!
