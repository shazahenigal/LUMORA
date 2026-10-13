import os
import sys
from django.core.wsgi import get_wsgi_application

# إضافة مسار المشروع الأساسي للـ Python path لكي يتعرف عليه Vercel
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

application = get_wsgi_application()

# مرادف مطلوب لـ Vercel
app = application  
