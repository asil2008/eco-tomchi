import os
from pathlib import Path
import dj_database_url # Buni o'rnatganingizga ishonch hosil qiling: pip install dj-database-url

# Yo'llar (Paths)
BASE_DIR = Path(__file__).resolve().parent.parent

# Xavfsizlik sozlamalari
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-o-&3q6u7-!&v_8*+v6p$88e9yq-2v')

# DEBUG faqat lokalda True bo'ladi, Render-da esa False
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS - Saytingiz manzillarini shu yerga yozing
ALLOWED_HOSTS = ['*'] # Yoki ['.onrender.com', 'localhost', '127.0.0.1']

# Ilovalar (Apps)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles', # Sizning ilovangiz
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Statik fayllar uchun (pip install whitenoise)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eco_tomchi.urls' # Loyihangiz nomi bilan mosligini tekshiring

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eco_tomchi.wsgi.application'

# MA'LUMOTLAR BAZASI (DATABASE)
# Render-dagi DATABASE_URL ni avtomatik ulaydi, bo'lmasa SQLite ishlatadi
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Parollarni tekshirish
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Til va vaqt
LANGUAGE_CODE = 'uz-uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# STATIK FAYLLAR (CSS, JS, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# WhiteNoise statik fayllarni siqish va keshda saqlash uchun
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media fayllar (Rasm yuklash uchun)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'