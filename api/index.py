import os
import sys

# إضافة مجلد الجذر إلى مسارات بايثون
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

# Vercel يتطلب تصدير التطبيق باسم app أو application
app = get_wsgi_application() 