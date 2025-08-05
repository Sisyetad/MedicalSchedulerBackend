# medicalschedulerbackend/celery.py

import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicalschedulerbackend.settings")

app = Celery("medicalschedulerbackend")

# Load config from Django settings using namespace CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks inside all apps
app.autodiscover_tasks()