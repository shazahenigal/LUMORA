import os
import sys
import traceback

# إضافة مسار المشروع
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumora_backend.settings')

try:
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as e:
    # طبع الخطأ المباشر على الشاشة ليعرفنا سبب الـ 404 أو الـ 500
    error_details = traceback.format_exc()
    def app(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, response_headers)
        return [f"PYTHON STARTUP ERROR:\n\n{error_details}".encode('utf-8')]  