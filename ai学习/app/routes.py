
# app/routes.py

from fastapi import APIRouter, HTTPException

from app.models import Task, TaskCreate
from app import services


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = services.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="任务不存在"
        )

    return task


@router.get("", response_model=list[Task])
def get_tasks(keyword: str | None = None):
    return services.get_all_tasks(keyword)


@router.post("", response_model=Task)
def create_task(task: TaskCreate):
    return services.create_task(task)
