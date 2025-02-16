from worker import celery_app, llama_model

import time


@celery_app.task(name="code_review.task", bind=True)
def generate_code_review(
    self,
    pr_code_diff: str,
    pr_url: str
):
    if llama_model is None:
        raise RuntimeError("failed loading model...")

    prompt = f"Review this code and provide feedback:\n{pr_code_diff}"
    output = llama_model(prompt)
    print(output)
    return output["choices"][0]["text"]


@celery_app.task(name="test", bind=True)
def long_running_task(
    self,
    param: int
) -> str:
    time.sleep(10)
    return f"Processed {param} successfully!"
