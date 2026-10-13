import os
import sys

# إضافة المسارات المطلوبة
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

# Vercel يتعرف على app أو application كـ handler
application = get_wsgi_application()
app = application 