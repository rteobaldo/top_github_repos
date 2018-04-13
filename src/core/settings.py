from unipath import Path
import dj_database_url
import environ

env = environ.Env()

BASE_DIR = Path(__file__).parent.parent.absolute()
PROJECT_DIR = BASE_DIR.child('core').absolute()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

if DEBUG:
    ALLOWED_HOSTS = ['0.0.0.0', 'localhost', env('HOST')]
else:
    ALLOWED_HOSTS = [env('HOST')]


# Application definition

INSTALLED_APPS = [
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'github',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR.child("templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

SITE_ID = 1

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LOCALE_NAME = 'pt_BR'

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANG = 'pt_BR'


# media url and folder to dynamic files
MEDIA_URL = "/media/"
MEDIA_ROOT = PROJECT_DIR.parent.child("media")

# static url and folder configs
STATIC_ROOT = PROJECT_DIR.parent.child("static")
STATIC_URL = '/static/'

# from static files folder
STATICFILES_DIRS = (
    BASE_DIR.child("assets"),
)

DEFAULT_FROM_EMAIL = 'admin@email.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

SHORT_DATETIME_FORMAT = "d/m/Y P"
DATETIME_FORMAT = "N j, Y, P"
TIME_FORMAT = "P"

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

if DEBUG:
   INTERNAL_IPS = ('127.0.0.1', 'localhost',)

ADMINS = (
  ('admin', 'admin@email.com'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/errors.log',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins', 'file'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}
