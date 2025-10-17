from celery import Celery
from backend.core.config import settings

# Create Celery app
# settings.REDIS_URL should be defined in your .env
app = Celery(
    "backend",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL  # optional if you want task result storage
)

# Optional: configure Celery (task serializer, timezone, etc.)
app.conf.update(
    result_expires=3600,
    task_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)
