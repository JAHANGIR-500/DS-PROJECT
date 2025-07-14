import os
import json
from pathlib import Path

# 🏗️ Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Security
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-default-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = json.loads(os.environ.get('DJANGO_ALLOWED_HOSTS', '["localhost"]'))
CSRF_TRUSTED_ORIGINS = json.loads(os.environ.get('CSRF_TRUSTED_ORIGINS', '[]'))

# 📦 Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'construction_department',
    'project',
]

# ⚙️ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Optional: Uncomment for static file serving in production
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 URLs
ROOT_URLCONF = 'dscp.urls'

# 🎨 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 WSGI application
WSGI_APPLICATION = 'dscp.wsgi.application'

# 🗄️ Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔒 Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'  # Adjusted to your region
USE_I18N = True
USE_TZ = True

# 📁 Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Uncomment for production with WhiteNoise

# 🆔 Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



