import os
import sys

# Add the parent directory of the 'MarAcademy' project to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from django.core.wsgi import get_wsgi_application

# Set the default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MarAcademy.settings")

# Expose the WSGI application
application = get_wsgi_application()
