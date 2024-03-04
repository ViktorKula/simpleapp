import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper01.settings')

app = Celery('NewsPaper01')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()

app.conf.beat_schedule = {
    'clear_mc_donalds_every_minute': {
        'task': 'mc_donalds.tasks.clear_old',
        'schedule': crontab(),
    },
}