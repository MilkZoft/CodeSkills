import os
import sys
sys.path.append('/home/czantany/public_html/CodeSkills')
os.environ['DJANGO_SETTINGS_MODULE'] = 'codeskills.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
