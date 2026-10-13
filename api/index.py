import os
import sys

# تحديد المسار الرئيسي للمشروع وإضافته لمسارات بايثون
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# إضافة مجلد الموديولات الداخلي إن وجد
LUMORA_DIR = os.path.join(BASE_DIR, 'lumora_backend')
if LUMORA_DIR not in sys.path:
    sys.path.append(LUMORA_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application() 