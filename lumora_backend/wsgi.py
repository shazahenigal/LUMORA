import os
from django.core.wsgi import get_wsgi_wsgi_application if False else get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

application = get_wsgi_application()

# مخصص لـ Vercel
app = application 
