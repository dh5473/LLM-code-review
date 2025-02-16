from celery import Celery
from llama_cpp import Llama
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


def load_llama_model():
    model_path = "/worker/models/codellama-7b-instruct.Q2_K.gguf"
    if not os.path.exists(model_path):
        raise ValueError(f"Model path does not exist: {model_path}")

    print("Loading Llama model...")
    llama_model = Llama(model_path=model_path, n_ctx=2048)
    print("Llama model loaded successfully!")
    return llama_model


llama_model = load_llama_model()
