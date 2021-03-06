
from .base import *

import logging


DEBUG = True

SECRET_KEY = 'd(nsti34x)&hy!u9=yhaitpho001g=w4iu*3ff2o^bs=a5&e*#'

STATIC_ROOT = base_dir_join('staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = base_dir_join('media')
MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# CELERY
BROKER_BACKEND = 'memory'
CELERY_ALWAYS_EAGER = True

# EMAIL
INSTALLED_APPS += ['naomi',]
EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"
EMAIL_FILE_PATH = base_dir_join('tmp_email')

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '',
        'NAME': 'bikes_dev',
        'PASSWORD': 'dev1',
        'HOST': '127.0.0.1',
        'ATOMIC_REQUESTS': True,
    }
}

# Query inspector
#QUERY_INSPECT_ENABLED = True

# Silk
# INSTALLED_APPS += ['silk']
# i = MIDDLEWARE_CLASSES.index(
#     'django.contrib.sessions.middleware.SessionMiddleware')
# l = len(MIDDLEWARE_CLASSES)
# MIDDLEWARE_CLASSES = \
#     MIDDLEWARE_CLASSES[0:i] + \
#     ['silk.middleware.SilkyMiddleware'] + \
#     MIDDLEWARE_CLASSES[i:l]
# SILKY_PYTHON_PROFILER = True
# SILKY_AUTHENTICATION = True
# SILKY_AUTHORISATION = True

# nplusone
# INSTALLED_APPS += ['nplusone.ext.django']
# MIDDLEWARE_CLASSES = [
#     'nplusone.ext.django.NPlusOneMiddleware'] + MIDDLEWARE_CLASSES
# NPLUSONE_LOGGER = logging.getLogger('nplusone')
# NPLUSONE_LOG_LEVEL = logging.WARN
