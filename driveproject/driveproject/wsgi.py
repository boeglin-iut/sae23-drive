"""
WSGI config for driveproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/django-app/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'driveproject.settings')

application = get_wsgi_application()
