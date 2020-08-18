from website.config.base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iubde98y983y4iubeflksjdhbcso8d[w039u1230ihjabsx!!!@(U@(u92009_(n'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['tomp-wg.org'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tomp_wg',
        'USER': 'tomp_wg',
	'PASSWORD': 'she!shells!windy!',
	'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
