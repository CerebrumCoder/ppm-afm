import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ppm_afm_web.settings')

# Ini bawaan Django (jangan dihapus)
application = get_wsgi_application()

# --- TAMBAHKAN BARIS INI SUPAYA VERCEL SENANG ---
app = application