from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_dev_database_name',
        'USER': 'your_dev_database_user',
        'PASSWORD': 'your_dev_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}