# Configuración de Seguridad - Webplayground

## 🔒 Datos Sensibles Protegidos

Este proyecto está configurado para proteger datos sensibles usando variables de entorno y `.gitignore`.

### ✅ Archivos Protegidos:
- `db.sqlite3` - Base de datos con información de usuarios
- `media/` - Archivos subidos por usuarios (avatares)
- `sent_emails/` - Emails de desarrollo
- `__pycache__/` - Archivos compilados de Python  
- `.DS_Store` - Archivos del sistema macOS
- `.env` - Variables de entorno sensibles

### 🔧 Configuración:

1. **Variables de Entorno**: Copiar `.env.example` a `.env`
```bash
cp .env.example .env
```

2. **Generar SECRET_KEY nueva**:
```python
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

3. **Configurar EMAIL** (opcional):
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
```

### 🚨 Importante:
- **NUNCA** commitear el archivo `.env`
- **NUNCA** exponer el `SECRET_KEY` en producción
- **SIEMPRE** usar `DEBUG=False` en producción
- **REVISAR** el `.gitignore` antes de hacer push

### 📋 Checklist de Seguridad:
- [x] SECRET_KEY en variables de entorno
- [x] DEBUG configurable via .env
- [x] Base de datos excluida del repositorio
- [x] Archivos de media excluidos
- [x] Archivos __pycache__ excluidos
- [x] Archivos .DS_Store excluidos
- [x] Emails de desarrollo excluidos

### 🔍 Verificar Seguridad:
```bash
# Verificar que no hay archivos sensibles en Git
git ls-files | grep -E "(secret|password|key|token|\.env|db\.sqlite3|media/|sent_emails/|__pycache__|\.DS_Store)"

# Debe devolver vacío o solo archivos seguros
```
