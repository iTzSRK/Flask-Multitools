# Configuración de desarrollo
DEBUG = True

# Rutas de archivos
UPLOAD_FOLDER = 'app/static/assets/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Configuración de seguridad
SESSION_COOKIE_SECURE = False  # Establecer a True en producción para habilitar cookies seguros
SESSION_COOKIE_HTTPONLY = True
