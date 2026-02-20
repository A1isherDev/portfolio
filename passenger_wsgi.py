import sys
import os

# Add the project directory to the sys.path
sys.path.append(os.getcwd())

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = "portfolio_project.settings"

# Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
