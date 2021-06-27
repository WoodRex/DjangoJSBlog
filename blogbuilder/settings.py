"""
Django settings for blogbuilder project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3$9@1w2#933slbs&5m=8hu#^$x)=52t)u@mo5(siamjd$-%@h8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'corsheaders',
    'haystack',
    'myaccount',
    'blog',
    'comment',
    'widget_tweaks',
    'compressor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.google',
]

# allauth相關設置
AUTHENTICATION_BACKENDS = (
      # django admin所使用的用户登陸與allauth無關 
      'django.contrib.auth.backends.ModelBackend',
      # allauth的身份驗證 
      'allauth.account.auth_backends.AuthenticationBackend',
)

# haystack相關
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    }
}

# django.contrib.sites需要的設置
SITE_ID = 1
# 指定要使用的登陸方法
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# 要求用戶注冊是必定要填寫email
ACCOUNT_EMAIL_REQUIRED = True
# 注冊後郵件驗證方法: "强制(mandatory)"、 "可選(optional)"
ACCOUNT_EMAIL_VERIFICATION = "None"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
# 更改或設置密碼后是否自動退出
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
# 登陸嘗試限制以及超時（throttle）
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1500

ACCOUNT_SIGNUP_REDIRECT_URL = "/accounts/profile/set_avatar/"
LOGIN_REDIRECT_URL = "/blog/index/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/blog/index/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = [
    # creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    # css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogbuilder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'libraries':{
            'lefttag': 'blog.templatetag.lefttag',

            }
        },
    },
]

WSGI_APPLICATION = 'blogbuilder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

"""
使用mysql配置請按以下方式
"""
# import pymysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('DJANGO_MYSQL_DATABASE') or 'blogbuilder',
#         'USER': os.environ.get('DJANGO_MYSQL_USER') or 'root',
#         'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD') or '123456',
#         'HOST': os.environ.get('DJANGO_MYSQL_HOST') or '127.0.0.1',
#         'PORT': int(os.environ.get('DJANGO_MYSQL_PORT') or 3306),
#         'OPTIONS': {'charset': 'utf8mb4'},
#     }
# }
# pymysql.version_info = (1, 4, 2, "final", 0)
# pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Email:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST') or 'smtp.gmail.com'
EMAIL_PORT = int(os.environ.get('DJANGO_EMAIL_PORT') or 465)
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

AUTH_USER_MODEL='myaccount.User'


# 跨域插件（上傳圖片時用）
# CORS_ALLOW_ALL_ORIGINS = True
