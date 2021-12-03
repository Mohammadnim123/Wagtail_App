from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r$ji%7wegjc*k4^9rr0=l+xp+ci4e%bbd@nq(92x*-6u3yh1t7'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [ #here we add something for Django Debuging Tool Bar
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [ #here we add something for Django Debuging Tool Bar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1") #here we add something for Django Debuging Tool Bar


try:
    from .local import *
except ImportError:
    pass
