from fastapi import APIRouter

from src.review.worker import celery_app

router = APIRouter(
    prefix="/api/review"
)


@router.post(
    "",
    tags=['code-review']
)
async def create_code_review(
    pr_diff: str,
    pr_url: str
):
    task_name = "code_review.task"
    task = celery_app.send_task(
        name=task_name,
        args=[pr_diff, pr_url]
    )

    return dict(
        id=task.id
    )


@router.get(
    "/{task_id}",
    tags=['code-review']
)
async def get_code_review(
    task_id: str
):
    # service
    return {"message": ""}