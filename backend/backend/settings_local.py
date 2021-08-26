# Debug settings, this is overwritten by settings_production in production.

DEBUG = True
SECRET_KEY = 'foo'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'backend']
CORS_ALLOWED_ORIGINS = ['http://localhost:3000']