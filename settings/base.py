# settings/base.py

import os
from pathlib import Path

# Load environment variables from .env file (optional)
from dotenv import load_dotenv
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(w2h!&e2sep24fl$587x%@85aq8!v@w!m06+z)j+=30g_at0rm'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

SESSION_SAVE_EVERY_REQUEST = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'attendance',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'attendance_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'attendance_system.wsgi.application'

# Database 설정은 development.py와 production.py에서 별도로 관리

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 이메일 백엔드 설정
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP 서버 주소
EMAIL_PORT = 587  # TLS 포트 (TLS 사용 시 587, SSL 사용 시 465)
EMAIL_USE_TLS = True  # TLS 사용 설정
EMAIL_USE_SSL = False  # SSL 미사용 (TLS와 동시에 사용할 수 없습니다)
EMAIL_HOST_USER = 'zend74@gmail.com'  # Gmail 주소
EMAIL_HOST_PASSWORD = 'zrbb vvxx sfwm xdad'  # Gmail 앱 비밀번호
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 기본 보내는 사람 주소

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'attendance', 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'  # 로그인 페이지 URL
LOGOUT_REDIRECT_URL = 'login'  # 로그아웃 후 리디렉션될 URL

# DEBUG 설정 (기본적으로 개발 환경에서는 True)
# DEBUG = os.environ.get('DEBUG', 'True') == 'True'
DEBUG = os.environ.get('DEBUG', 'True').lower() in ['true', '1']

# 로그 디렉토리와 파일 설정
LOG_FILE = os.path.join(BASE_DIR, 'debug.log')

# 서버가 시작될 때 로그 파일 비우기
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w'):
        pass  # 파일을 열고 내용 비우기


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',  # 모든 로그 메시지를 출력하도록 DEBUG로 설정합니다.
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',  # 모든 로그 메시지를 파일로 저장하도록 DEBUG로 설정합니다.
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
            'encoding': 'utf-8',  # UTF-8 인코딩 사용
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # Django 관련 모든 로그 메시지를 출력합니다.
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # 요청 관련 모든 로그 메시지를 출력합니다.
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # DB 쿼리 로그 메시지를 출력합니다.
            'propagate': False,
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # root 로거의 모든 로그 메시지를 출력합니다.
        },
    },
}
