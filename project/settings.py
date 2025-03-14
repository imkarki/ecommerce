"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

#Update settings.py to use .env
import environ
import os

#for cloudinary (to upload the image (media) from the  
import cloudinary
import cloudinary.uploader
import cloudinary.api



from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1lm%f+z__ws+=vwzva!x4)iif!pw_=8m$x&%=%2wlks@pe(or7'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False

# DEBUG=True

ALLOWED_HOSTS = ['ecommerce-rbcl.onrender.com','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'cloudinary',
    'cloudinary_storage',
]

#written by myself for login,logout and registration
AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend'
]

#written by self for CustomerUserModel
#AUTH_USER_MODEL='app.CustomUser'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this after installation of whitenoise
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/media/'
#MEDIA_ROOT=BASE_DIR / 'media'   # Directory to store user-uploaded media files

#to show images in render 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Store uploaded files in 'media' directory

# to show in render static files 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Collect static files here in production

# Enable WhiteNoise compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    BASE_DIR / 'app/static',  # Add this line if you have a `static` folder at the root of your project
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # This is where static files will be collected in production

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# can create conflict 
# STATICFILES_DIRS=[
#     BASE_DIR,"static"
# ]


# LOGOUT_REDIRECT_URL='/index/'
#LOGIN_REDIRECT_URL='/dashboard/'

EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"


#for the payment
# ESEWA_PRODUCT_CODE="EPAYTEST"  # Replace with actual product code if in production
# ESEWA_SECRET_KEY="8gBm/:&EnhH.1/q"
# ESEWA_SUCCESS_URL="http://yourdomain.com/success/"
# ESEWA_FAILURE_URL="http://yourdomain.com/failure/"

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default session backend


#for login 
#LOGIN_URL='login_views'  # Redirects to login if user is not authenticated


LOGIN_URL='/loginview/'

#LOGIN_REDIRECT_URL = '/'  # Redirect to home instead of login


# 8gBm/:&EnhH.1/q(
    
    
# for email 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))  # Load .env file

DEBUG = env.bool("DEBUG", default=False)   #pahile False thiyo

# Email Configuration
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



#EMAIL_HOST_USER = 'ambukarki01@gmail.com'  # Your email
#EMAIL_HOST_PASSWORD = 'nvvfpfxxxqzhbjkq'  # Use an App Password, not your real password


# CLOUDINARY_URL="cloudinary://962641844214638:6THBW1UETbstw3J9pKIg_4RUfkE@dtvfgiohr"

# # Cloudinary settings
# cloudinary.config( 
#   cloud_name='dtvfgiohr', 
#   api_key='962641844214638', 
#   api_secret='6THBW1UETbstw3J9pKIg_4RUfkE',
# )


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Cloudinary Configuration
# CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

CLOUDINARY_URL = env("CLOUDINARY_URL", default="")

if CLOUDINARY_URL:
    cloudinary.config(
        cloud_name=CLOUDINARY_URL.split("@")[1],
        api_key=CLOUDINARY_URL.split("//")[1].split(":")[0],
        api_secret=CLOUDINARY_URL.split(":")[2].split("@")[0],
    )