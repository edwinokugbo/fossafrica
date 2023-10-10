from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DEVSECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.getenv('DEVHOST'), '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': os.getenv('django.db.backends.postgresql'),
        'ENGINE': os.getenv('DEVENGINE'),
        'NAME': os.getenv('DEVDBNAME'),
        'USER': os.getenv('DEVUSER'),
        'PASSWORD': os.getenv('DEVPASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'html', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'html', 'media')

# Email Params Section
#DEFAULT_FROM_EMAIL = 'edwin@edwin-Aspire-VN7-571G'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'edwin@edwin-Aspire-VN7-571G'

# SignUp/Login/Authentication
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.MySignupForm',
}
ACCOUNT_SIGNUP_REDIRECT_URL = '/'

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8080", "https://127.0.0.1:8080"]