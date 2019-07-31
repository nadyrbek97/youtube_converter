import os
from celery import Celery

# set the default Django setting module for the 'celery' command line program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_converter.settings')
# create an instance of the application
app = Celery('youtube_converter')
# load custom configuration from out project settings
# namespace attribute specifies the prefix that Celery-related settings will have in our settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')
# we said celery to auto-discover asynchronous tasks for our application
# Celery will look for a 'tasks.py' file in each application directory
app.autodiscover_tasks()
