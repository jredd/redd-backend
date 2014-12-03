"""
Django settings for redd project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
PROJECT_ROOT = BASE_DIR.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sr@l3mh!t@du1k3p0p3_g&^#^+yj!0pa7!x73$kk_fa$mn9^3-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Downloaded Modules
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    # 'provider',
    # 'provider.oauth2',
    # 'require',

    # Local Apps
    'user_auth',
    # 'tracker',
    # 'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

CORS_ORIGIN_WHITELIST = (
        'localhost:63343',
        # 'http://localhost',
        # 'http://127.0.0.1:8000/',
        # 'http://127.0.0.1:8000',
    )
# CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'redd.urls'

WSGI_APPLICATION = 'redd.wsgi.application'

AUTH_USER_MODEL = 'user_auth.CustomUser'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(PROJECT_ROOT / 'db.sqlite3'),
    }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.OAuth2Authentication',
    )
}

LOGIN_REDIRECT_URL = 'admin:index'
LOGOUT_REDIRECT_URL = 'auth_views.login'


SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (str(PROJECT_ROOT / 'templates'),)
# TEMPLATE_DIRS = ('templates')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
                       "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATICFILES_DIRS = (
    str(PROJECT_ROOT / 'static'),
)

STATIC_ROOT = str(PROJECT_ROOT.parent / 'static')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'require.storage.OptimizedStaticFilesStorage'

# EMAIL_BACKEND = 'django_ses.SESBackend'
# EMAIL_FROM = 'sister@sister.tv'
# EMAIL_HOST_USER = 'sister@sister.tv'
# DEFAULT_FROM_EMAIL = 'sister@sister.tv'
# SERVER_EMAIL = 'sister@sister.tv'
