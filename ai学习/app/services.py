
# app/services.py

from app.models import Task, TaskCreate


# 暂时使用内存保存任务
tasks = [
    Task(id=1, title="学习 Python", done=False),
    Task(id=2, title="学习 HTTP", done=False),
    Task(id=3, title="学习 FastAPI", done=False)
]


def get_task_by_id(task_id: int) -> Task | None:
    for task in tasks:
        if task.id == task_id:
            return task

    return None


def get_all_tasks(keyword: str | None = None) -> list[Task]:
    if keyword is None:
        return tasks.copy()

    result = []

    for task in tasks:
        if keyword.lower() in task.title.lower():
            result.append(task)

    return result


def create_task(data: TaskCreate) -> Task:
    new_id = max((task.id for task in tasks), default=0) + 1

    new_task = Task(
        id=new_id,
        title=data.title,
        done=data.done
    )

    tasks.append(new_task)

    return new_task
