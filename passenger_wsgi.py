import sys
import os
import traceback

# 1. Set the project path
project_path = os.getcwd()
if project_path not in sys.path:
    sys.path.append(project_path)

# 2. Add potential virtualenv paths
# Serv00 users often place venv in home or project root
home_dir = os.path.expanduser('~')
possible_venvs = [
    os.path.join(home_dir, 'venv'),
    os.path.join(home_dir, '.venv'),
    os.path.join(project_path, 'venv'),
    os.path.join(project_path, '.venv'),
]

# We'll try to find any site-packages folder in these common locations
for venv in possible_venvs:
    if os.path.exists(venv):
        # Look for site-packages in common python version subdirectories
        # Or just append based on a glob-like check if needed
        # For simplicity, we'll try a few versions or look for the folder
        lib_path = os.path.join(venv, 'lib')
        if os.path.exists(lib_path):
            for py_dir in os.listdir(lib_path):
                site_pkgs = os.path.join(lib_path, py_dir, 'site-packages')
                if os.path.exists(site_pkgs):
                    if site_pkgs not in sys.path:
                        sys.path.insert(0, site_pkgs)

# 3. Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = "portfolio_project.settings"

# 4. Error Logging (Helpful for debugging on Serv00)
DEBUG_LOG = os.path.join(project_path, 'passenger_debug.log')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception:
    with open(DEBUG_LOG, 'a') as f:
        f.write("\n--- ERROR AT " + os.popen('date').read().strip() + " ---\n")
        f.write("PYTHON VERSION: " + sys.version + "\n")
        f.write("SYS PATH: " + str(sys.path) + "\n")
        f.write(traceback.format_exc())
    raise
