from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['clinicodentistasv.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    #'default': {
        #'ENGINE': 'mysql_cymysql', 
        #'NAME': '',
        #'USER': '',
        #'PASSWORD': '',
        #'HOST': '',   
        #'PORT': '3306',
        #'OPTIONS' :  { 
        #    'init_command' :  "SET sql_mode = 'STRICT_TRANS_TABLES'" , 
       # }, 
    #}
}

STATICFILES_DIRS = (BASE_DIR, 'static')