import sys
import os

# Add your project directory to the sys.path
project_home = '/home/mba0329/university_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'university_project.settings'

# Activate your virtual environment
activate_this = '/home/mba0329/.virtualenvs/universityenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django's WSGI application to handle requests
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()