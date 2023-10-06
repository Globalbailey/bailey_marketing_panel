from gmcmarketing.settings import *
from decouple import config


ALLOWED_HOSTS = ['web-gmc.up.railway.app', 'web-production-0f4e.up.railway.app', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://web-gmc.up.railway.app']

SECRET_KEY = config('SECRET_KEY')

# Get the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the path to Chromedriver executable
CHROMEDRIVER_PATH = os.path.join(BASE_DIR, 'bin', 'chromedriver')

# Set the path to Chrome browser binary
GOOGLE_CHROME_BIN = os.path.join(BASE_DIR, 'bin', 'chrome')

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
