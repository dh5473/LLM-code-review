from celery import Celery
# from pymongo import MongoClient
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

celery_app = Celery(
    "worker",
    broker=f"redis://{REDIS_HOST}:{REDIS_PORT}",
    backend=f"redis://{REDIS_HOST}:{REDIS_PORT}",
)

celery_app.conf.update(
    broker_connection_retry_on_startup=True,
    result_expires=120000,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Seoul",
    enable_utc=True,
)

# MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
# client = MongoClient(MONGO_URI)
# db = client["code_review"]
# collection = db["reviews"]
