
# main.py

from fastapi import FastAPI
from app.routes import router as task_router


app = FastAPI(
    title="AI 学习任务管理系统",
    version="1.0.0"
)


app.include_router(task_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}