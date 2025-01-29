from pathlib import Path
import os
from decouple import Config, RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Указываем путь к .env.dev
ENV_FILE = os.path.join(BASE_DIR, '.env.dev')

# Загружаем переменные из .env.dev
config = Config(RepositoryEnv(ENV_FILE))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', cast=bool)

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS').split(',')


# Application definition
INSTALLED_APPS = [
    # default apps
    'django.contrib.admin',       # Панель администратора Django
    'django.contrib.auth',        # Система аутентификации и пользователей
    'django.contrib.contenttypes',  # Поддержка типов контента
    'django.contrib.sessions',    # Управление пользовательскими сессиями
    'django.contrib.messages',    # Система сообщений
    'django.contrib.staticfiles',  # Обслуживание статических файлов

    # 3rd party apps
    'rest_framework',             # Django REST Framework (API)
    'channels',                   # Поддержка WebSockets (реальное время)
    'django_celery_beat',         # Планировщик задач Celery

    # project apps
    'battle',    # Боевая система (PvP, PvE, управление боями)
    'chat',      # Чаты (общие, кланы, личные сообщения)
    'heroes',    # Персонажи, их прокачка, казарма
    'inventory',  # Инвентарь, скины, ресурсы
    'clans',     # Кланы, управление кланами
    'notifications',  # Система уведомлений (Celery + WebSockets)
    'users',     # Управление пользователями (профиль, настройки)

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'battleforge.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'battleforge.wsgi.application'


# postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT', cast=int),
    }
}

# redis
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(config('REDIS_HOST'), config('REDIS_PORT', cast=int))],
        },
    },
}

# celery
CELERY_BROKER_URL = config('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
