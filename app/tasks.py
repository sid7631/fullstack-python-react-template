from celery import Celery
import logging
import os
import time

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
celery.conf.accept_content = ['application/text','json']

logger = logging.getLogger(__name__)

#demo task
def get_task_status(task_id):
    result = celery.AsyncResult(task_id)
    return result

@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True