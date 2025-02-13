from worker import celery_app
import time


@celery_app.task(name="code_review.task", bind=True)
def process_code_review(
    self,
    pr_diff: str,
    pr_url: str
):
    print(f"Processing review for PR {pr_url}")
    return f"Review processed for {pr_url}"


@celery_app.task(name="test", bind=True)
def long_running_task(
    self,
    param: int
) -> str:
    time.sleep(10)
    return f"Processed {param} successfully!"
