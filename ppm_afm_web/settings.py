"""
Django settings for ppm_afm_web project.
Modified for Vercel + Neon + Cloudinary
"""

import os
from pathlib import Path
import dj_database_url


# Kebutuhan integrasi web
# 1. Neon.tech
# Connection string: psql 'postgresql://neondb_owner:npg_Zb79KOEwItTu@ep-wispy-union-a1z5mjlt-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require' (Database URL)
# 2. Cloudinary (media)
# Cloud Name: dhkvqtm9s
# Cloudinary API Key: 163388715733427
# API Secret: lmjWjKQ5zy2o-qYP9-_4iCdfX5A

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- KONFIGURASI KEAMANAN & ENVIRONMENT ---

# Secret Key ambil dari Environment Variable (Aman), kalau di laptop pakai default
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-dev-key-hancurkan-saja")

# Debug otomatis False kalau ada di Vercel, True kalau di laptop
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Host yang diizinkan
ALLOWED_HOSTS = ["*"] # Boleh "*" untuk awal, atau ".vercel.app" nanti

# Penting buat Vercel supaya bisa Login Admin / Post Data
CSRF_TRUSTED_ORIGINS = ["https://" + os.environ.get("VERCEL_URL", "127.0.0.1")]

# Application definition
INSTALLED_APPS = [
    # Apps Bawaan
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
    # 3rd Party (PENTING: Urutan Cloudinary)
    'cloudinary_storage', # Harus sebelum staticfiles jika pakai static cloudinary (opsional)
    'django.contrib.staticfiles',
    'cloudinary', # Harus ada

    # Apps Kamu
    "news_ppm",
    "pages_ppm",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # PENTING BUAT VERCEL
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ppm_afm_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ppm_afm_web.wsgi.application'

# --- DATABASE (Logika Ganda) ---

# Cek apakah ada DATABASE_URL (artinya sedang di Vercel/Prod)
i# Pakai SQLite (Aman & Permanen)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- CLOUDINARY (Media Storage) ---

# Konfigurasi Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# Jika variabel CLOUDINARY ada, gunakan Cloudinary sebagai penyimpanan Media
# GANTI LOGIKANYA JADI INI:
if 'DATABASE_URL' in os.environ:
    # Sedang di Vercel? WAJIB pakai Cloudinary (walaupun key-nya mungkin belum pas, setidaknya dia nyoba ke sana)
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    # Sedang di Laptop? Pakai lokal
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC & MEDIA FILES ---

# Setup Folder Lokal (Gambar kesimpen di server)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Login settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'news:article_admin_list'
LOGOUT_REDIRECT_URL = 'pages:home'