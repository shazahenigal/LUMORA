import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

from django.core.wsgi import get_wsgi_application

# Vercel يعتمد كلياً على متغير باسم app
app = get_wsgi_application() 
