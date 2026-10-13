import os
import sys

# إضافة المسار الحالي والمجلد الرئيسي للـ sys.path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

# استدعاء تطبيق الـ WSGI وتصديره كـ app
application = get_wsgi_application()
app = application 