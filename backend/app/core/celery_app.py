from celery import Celery
from app.core.config import settings

celery_app = Celery("gametracker", broker=settings.celery_broker_url, backend=settings.celery_result_backend, include=["app.tasks.ai_tasks"])
celery_app.conf.update(task_track_started=True, task_time_limit=300, worker_prefetch_multiplier=1)
