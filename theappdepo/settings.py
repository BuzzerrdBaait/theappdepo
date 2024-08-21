
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY=os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*',]

INSTALLED_APPS = [
    'flashcards',
    'ilovecookbooks',
    'profiles',
    'home_page',
    'experimental_playground',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'theappdepo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates','profiles'),
            os.path.join(BASE_DIR,'templates','ilovecookbooks'),
            os.path.join(BASE_DIR,'templates','flashcards'),
            os.path.join(BASE_DIR,'templates','home_page'),
            os.path.join(BASE_DIR,'templates', 'experimental_playground')
        ],   

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

WSGI_APPLICATION = 'theappdepo.wsgi.application'

STATICFILES_DIRS=[
     os.path.join(BASE_DIR,'static'),
    ]

SCHEMA_NAME=os.environ.get('SCHEMA_NAME')
DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')

AUTH_USER_MODEL = 'profiles.User_Profile'

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SCHEMA_NAME,
        'USER' : DB_USER,
        'PASSWORD' : DB_PASSWORD,
        'HOST' : '127.0.0.1',
        'PORT' : '3306',

        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
          }
     }


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT=os.path.join(BASE_DIR,"/static/") 

MEDIA_URL=os.path.join(BASE_DIR,"media/")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
