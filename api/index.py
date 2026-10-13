import os
import sys

# إضافة مسار المشروع الحالي إلى مسارات بايثون
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

# إعداد متغير البيئة لدجانجو
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

# تعريف تطبيق الـ WSGI بصيغة app المعتمدة لدى Vercel
app = get_wsgi_application() 