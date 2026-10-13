import os
import sys

# إضافة مجلد المشروع الرئيسي إلى مسار بايثون
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

# Vercel Serverless Function Entry Point
app = get_wsgi_application() 