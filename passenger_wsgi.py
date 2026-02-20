import sys
import os

# Set the project path
project_path = os.getcwd()
sys.path.append(project_path)

# Point to your virtualenv if you are using one
# Replace 'venv' with your actual virtualenv directory name
# Generally on Serv00 it is in your home directory
venv_path = os.path.expanduser('~/venv/lib/python3.12/site-packages') # Check your python version!
if os.path.exists(venv_path):
    sys.path.insert(0, venv_path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = "portfolio_project.settings"

# Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
