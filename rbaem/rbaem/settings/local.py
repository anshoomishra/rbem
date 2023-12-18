from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = bool(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase.sqlite',
    }
}

AWS_REGION = os.environ.get('AWS_REGION')  # e.g., 'us-east-1'
AWS_SNS_TOPIC_ARN = os.environ.get('AWS_SNS_TOPIC_ARN')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')