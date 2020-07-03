import os

from django.utils.translation import gettext_lazy as _
from unipath import Path

SECRET_KEY = ''
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '192.168.*', '*']

BASE_DIR = Path(__file__).parent.parent.parent

ROOT_URLCONF = 'apps.Application.urls'

# Application definition

INSTALLED_APPS = [
    'apps.Application',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates/', '../templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]

WSGI_APPLICATION = 'apps.wsgi.application'

# You can change the default anytime
DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('data').child('sqlite').child('db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django-password',
        'HOST': 'mysql',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

LANGUAGE_CODE = 'en-US'
# LANGUAGE_CODE = 'de-DE'


LANGUAGES = [
    ('en', _('English')),
    # ('de', _('German')),
]

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.y H:i:s'

TIME_ZONE = 'Europe/Berlin'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))


STATICFILES_DIRS = (
    BASE_DIR.child('assets'),
)

STATIC_ROOT = BASE_DIR.child('static')
STATIC_URL = '/static/'

LOCALE_PATHS = [
    BASE_DIR.child('locale'),
]


MEDIA_ROOT = BASE_DIR.child('data').child('media')
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@example.com'
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = 'noreply@example.com'
DEFAULT_FROM_EMAIL = 'noreply@example.com'
EMAIL_USE_SSL = True
# EMAIL_USE_TLS = True

# @todo Is this in use?
ADMINS = [
    ("Administrator", "staff@example.com")
]

AUTH_USER_MODEL = 'Application.CustomUser'

SETTINGS_EXPORT = [
    'ENV',
    'EMAIL_HOST_USER',
    'AUTH_USER_MODEL',
    'DEFAULT_CONTACT_PERSON',
    'LANGUAGES'
]
