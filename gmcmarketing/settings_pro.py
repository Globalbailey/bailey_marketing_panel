from gmcmarketing.settings import *
from decouple import config


ALLOWED_HOSTS = ['web-gmc.up.railway.app', 'web-production-0f4e.up.railway.app', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://web-gmc.up.railway.app']

SECRET_KEY = config('SECRET_KEY')


# Production database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Add any other production-specific settings here
