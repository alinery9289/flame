"""
Django settings for DjangoTest project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hh_rhr#7%=qfe0t71+*xsck2($=$(2dp(s@=qlyyt(i_vb(#+7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'learn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'DjangoTest.urls'

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

WSGI_APPLICATION = 'DjangoTest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'medialab_513',
        'HOST': '202.120.39.226',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# -----------------------------------------------------------------------
# djcelery conf
# -----------------------------------------------------------------------
CELERY_TIMEZONE = 'Asia/Shanghai'

# -------------------------------------------------------------------
#                     Celery Periodic Tasks
# -------------------------------------------------------------------
from datetime import timedelta
from celery.schedules import crontab

CELERY_IMPORTS = ("learn.tasks")

CELERYBEAT_SCHEDULE = {
        # Executes every Monday morning at 7:30 A.M
        'del-image-every-night': {
            'task': 'learn.tasks.recognize_image',
            #'schedule': crontab(hour=7, minute=30, day_of_week=1),

            # schedule every 1 minute
            #'schedule': crontab(minute='*/1'),

            # schedule every 5 seconds
            'schedule': timedelta(seconds=5),

            'args': (16,),
            },
        }


# scenario 1: local host configuration
# BROKER_URL = 'amqp://'
# CELERY_RESULT_BACKEND = 'amqp://'

# scenario 2: distributed, multiple hosts
# the web server (django node) IP address
BROKER_URL = 'amqp://guest:guest@172.16.6.157:5672'
CELERY_RESULT_BACKEND = 'amqp://'

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"

# -------------------------------------------------------------------
#                    Celery Task Queue Settings
# -------------------------------------------------------------------
# the worker can specify which queue to listen to by -Q option,
# e.g, run a worker and listening to the 'priority.high' queue:
# "python manager.py celery worker -Q priority.high"

# CELERY_ROUTES = {
#         'learn.tasks.stabilize_video': {'queue': 'video.stabilization'},
#         'learn.tasks.recognize_image': {'queue': 'image.recognition'}
# }
