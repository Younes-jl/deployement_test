"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application() 

# app = application

import sys
import os

# Chemin vers le dossier contenant manage.py (ton projet principal)
project_home = '/home/younes123/Event-management-final-version-'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Indiquer à Django où trouver les settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
