import os
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'User',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'simple_history',
    'Admin',
    'Role',
    'Branch',
    'Doctor',
    'Patient',
    'Receptionist',
    'Queue',
    'Diagnosis',
    'drf_spectacular',
]

AUTH_USER_MODEL = 'User.UserModel'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'medicalschedulerbackend.core.middleware.redis_cache_middleware.RedisCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'medicalschedulerbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'medicalschedulerbackend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default='5432'),
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# ]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
}

FIELD_ENCRYPTION_KEY = config('FIELD_ENCRYPTION_KEY')

SIMPLE_HISTORY_HISTORY_USER_MODEL = 'User.UserModel'


# SECURE_SSL_REDIRECT = True  # Redirect all HTTP to HTTPS.
# SECURE_HSTS_SECONDS = 3600  # Enables Strict-Transport-Security.
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True



# SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default
# SESSION_COOKIE_NAME = 'sessionid'





# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware', # needed for `request.user`
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'simple_history.middleware.HistoryRequestMiddleware',
# ]

# if 'RUNNING_ADMIN' in os.environ:
#     MIDDLEWARE += [
#         'django.contrib.sessions.middleware.SessionMiddleware',
#         'django.middleware.csrf.CsrfViewMiddleware',
#         'django.contrib.messages.middleware.MessageMiddleware',
#     ]


SPECTACULAR_SETTINGS = {
    'TITLE': 'Medical Scheduler API',
    'DESCRIPTION': 'API for scheduling medical appointments',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL', default='redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 'PARSER_CLASS': 'redis.connection.HiredisParser',
            'TIMEOUT': 60,
        },
    }
}