import os
import sys

# إضافة المسار الجذري للمشروع لبيئة بايثون
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

# تعريف المتغير الأساسي app الذي يبحث عنه Vercel
app = get_wsgi_application() 