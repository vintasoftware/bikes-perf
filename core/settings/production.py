from decouple import config
import appenlight_client.client as e_client

from .base import *

DEBUG = False

SECRET_KEY = config('SECRET_KEY', default='')

# TODO - Set the allowed hosts

INSTALLED_APPS += ('opbeat.contrib.django',)
MIDDLEWARE_CLASSES += \
    ['opbeat.contrib.django.middleware.OpbeatAPMMiddleware'] + \
    MIDDLEWARE_CLASSES

OPBEAT = {
    'ORGANIZATION_ID': config('OPBEAT_ORGANIZATION_ID', default=''),
    'APP_ID': config('OPBEAT_APP_ID', default=''),
    'SECRET_TOKEN': config('OPBEAT_SECRET_TOKEN', default=''),
}

APPENLIGHT = e_client.get_config(
    {'appenlight.api_key': config('APPENLIGHT_PRIVATE_KEY', default='')})

MIDDLEWARE_CLASSES += \
    ['appenlight_client.django_middleware.AppenlightMiddleware'] + \
    MIDDLEWARE_CLASSES

# STORAGES
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = base_dir_join('staticfiles')
STATIC_URL = '/static/'

# CELERY
BROKER_URL = config('REDIS_URL', default='')
CELERY_RESULT_BACKEND = config('REDIS_URL', default='')
CELERY_SEND_TASK_ERROR_EMAILS = True

# EMAIL
SERVER_EMAIL = config('SERVER_EMAIL', default='')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')


from dj_database_url import parse as db_url

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url)
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': base_dir_join('django.log'),
        },
        'opbeat': {
            'level': 'WARNING',
            'class': 'opbeat.contrib.django.handlers.OpbeatHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'opbeat.errors': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
