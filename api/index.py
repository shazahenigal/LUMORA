import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

try:
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as e:
    # لو حصل أي خطأ في إقلاع دجانجو، هنطبع تفاصيل الخطأ مباشرة
    import traceback
    print("DJANGO STARTUP ERROR:", traceback.format_exc())
    raise e 