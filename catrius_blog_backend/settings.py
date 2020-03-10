"""
Django settings for catrius_blog_backend project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    SECRET_KEY=(str, ''),
    DATABASE_URL=(str, ''),
    ALLOWED_HOSTS=(list, []),
    CORS_ORIGIN_WHITELIST=(list, []),
    AWS_ACCESS_KEY_ID=(str, ''),
    AWS_SECRET_ACCESS_KEY=(str, ''),
    AWS_S3_REGION_NAME=(str, ''),
    AWS_STORAGE_BUCKET_NAME=(str, ''),
    DEFAULT_FILE_STORAGE=(str, 'django.core.files.storage.FileSystemStorage'),
    STATICFILES_STORAGE=(str, 'django.contrib.staticfiles.storage.StaticFilesStorage'),
    STATIC_ROOT=(str, None),
    MEDIA_ROOT=(str, ''),
    MEDIA_URL=(str, ''),
)

# reading .env file
environ.Env.read_env('.env')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LIBRARY_APPS = [
    'rest_framework',
    'django_extensions',
    'corsheaders',
    'watson',
    'storages',
]

LOCAL_APPS = [
    'blog',
]

INSTALLED_APPS = DJANGO_APPS + LIBRARY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'catrius_blog_backend.urls'

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

WSGI_APPLICATION = 'catrius_blog_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': env.db()
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = env('STATIC_ROOT')
# This is required by django.contrib.staticfiles. In production, it is ignored by django-storage.
STATIC_URL = '/static/'
MEDIA_ROOT = env('MEDIA_ROOT')
MEDIA_URL = env('MEDIA_URL')

# A list of origins that are authorized to make cross-site HTTP requests
# https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST')

# Custom Rest Framework pagination
# https://www.django-rest-framework.org/api-guide/pagination/
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'blog.pagination.CountedPageNumberPagination',
    'PAGE_SIZE': 12
}

# AWS
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_OBJECT_PARAMETERS = {
     'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = None

# Storage
DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
STATICFILES_STORAGE = env('STATICFILES_STORAGE')
