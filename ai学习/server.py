
from fastapi import FastAPI, HTTPException
from app.models import Task, TaskCreate

app = FastAPI()




# 暂时使用内存保存数据
tasks = [
    Task(id=1, title="学习 Python", done=False),
    Task(id=2, title="学习 HTTP", done=False),
    Task(id=3, title="学习 FastAPI", done=False)
]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="任务不存在"
    )


@app.get("/tasks")
def get_tasks(keyword: str | None = None):
    if keyword is None:
        return tasks

    result = []

    for task in tasks:
        if keyword.lower() in task.title.lower():
            result.append(task)

    return result


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_id = max((t.id for t in tasks), default=0) + 1

    new_task = Task(
        id=new_id,
        title=task.title,
        done=task.done
    )

    tasks.append(new_task)

    return new_task
