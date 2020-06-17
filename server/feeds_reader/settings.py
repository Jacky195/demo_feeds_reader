import os

DEPLOYMENT_ENV = os.environ.get('DEPLOYMENT_ENV')
if DEPLOYMENT_ENV == 'development':
    from feeds_reader.settings_development import *
elif DEPLOYMENT_ENV == 'staging':
    from feeds_reader.settings_staging import *
elif DEPLOYMENT_ENV == 'production':
    from feeds_reader.settings_production import *
else:
    print("Invalid deployment environment")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'crawlers.apps.CrawlersConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:3548',  # dev - client admin
    'http://localhost:6584',  # staging - client admin
    'http://localhost:8562',  # production - client admin
]


ROOT_URLCONF = 'feeds_reader.urls'

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

WSGI_APPLICATION = 'feeds_reader.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT')
    }
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://feeds_reader_cache_redis_{}:6379/1".format(DEPLOYMENT_ENV),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "joinus_{}".format(DEPLOYMENT_ENV)
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'



# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] [%(asctime)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'error.log'),
            'maxBytes': 1024*1024*5,  # 5MB
            'backupCount': 10,
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'debug.log'),
            'maxBytes': 1024*1024*5,  # 5MB
            'backupCount': 10,
        },
    },
    'loggers': {
        'crawlers': {
            'handlers': ['file_debug', 'file_error', 'console'],
            'level': 'DEBUG'
        }
    }
}


# Fetched Sites
FEED_SITES = [
    'crawlers.sites.washingtonpost',
    'crawlers.sites.feedforall'
]


CACHE_TIMEOUT_UNTIL_DELETED = None  # never expire unless being deleted manually by code
CACHE_TIMEOUT_AUTO = 60*60  # 60 minutes
