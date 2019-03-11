# -*- coding: utf-8 -*-
import os, sys
sys.path.append('/home/g/gyzallj0/neutralmike/HelloDjango')
sys.path.append('/home/g/gyzallj0/.local/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloDjango.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

