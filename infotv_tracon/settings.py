import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '9()(lzm)jdr$szjfdx8^^#j_6efj@d&$9pb6l2h&=udxom3(bn'

DEBUG = True
TEMPLATE_DEBUG = True

def mkpath(*parts):
    return os.path.abspath(os.path.join(BASE_DIR, *parts))

if DEBUG:
    # XXX Monkey patch is_secure_transport to allow development over insecure HTTP

    from warnings import warn
    warn(UserWarning("Monkey_patching oauthlib.oauth2:is_secure_transport to allow OAuth2 over HTTP. Never do this in production!"))

    fake_is_secure_transport = lambda token_url: True

    import oauthlib.oauth2
    import requests_oauthlib.oauth2_session
    import oauthlib.oauth2.rfc6749.parameters
    import oauthlib.oauth2.rfc6749.clients.base

    for module in [
        oauthlib.oauth2,
        requests_oauthlib.oauth2_session,
        oauthlib.oauth2.rfc6749.parameters,
        oauthlib.oauth2.rfc6749.clients.base,
    ]:
        module.is_secure_transport = fake_is_secure_transport

ALLOWED_HOSTS = ['infotv.tracon.fi']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'kompassi_oauth2',
    'infotv',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'kompassi_oauth2.backends.KompassiOAuth2AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'infotv_tracon.urls'

WSGI_APPLICATION = 'infotv_tracon.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'infotv_tracon.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'celery': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True
        },
        'kompassi_oauth2': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True
        },
    }
}

LANGUAGE_CODE = 'fi-fi'

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = mkpath('static')

KOMPASSI_INSTALLATION_SLUG = 'turskadev'
KOMPASSI_HOST = 'http://kompassi.dev:8000'
KOMPASSI_OAUTH2_AUTHORIZATION_URL = '{KOMPASSI_HOST}/oauth2/authorize'.format(**locals())
KOMPASSI_OAUTH2_TOKEN_URL = '{KOMPASSI_HOST}/oauth2/token'.format(**locals())
KOMPASSI_OAUTH2_CLIENT_ID = 'kompassi_insecure_test_client_id'
KOMPASSI_OAUTH2_CLIENT_SECRET = 'kompassi_insecure_test_client_secret'
KOMPASSI_OAUTH2_SCOPE = ['read']
KOMPASSI_API_V2_USER_INFO_URL = '{KOMPASSI_HOST}/api/v2/people/me'.format(**locals())
KOMPASSI_API_V2_EVENT_INFO_URL_TEMPLATE = '{kompassi_host}/api/v2/events/{event_slug}'
KOMPASSI_ADMIN_GROUP = 'admins'
KOMPASSI_EDITOR_GROUP = 'infotv-staff'

LOGIN_URL = '/oauth2/login' if 'kompassi_oauth2' in INSTALLED_APPS else '/admin/login/'
LOGOUT_URL = '/admin/logout/'

INFOTV_DEFAULT_EVENT_SLUG = 'traconx'
INFOTV_POLICY_CLASS = 'infotv_tracon.policy.TraconPolicy'
