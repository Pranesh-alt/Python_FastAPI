from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from modules.Tasks.services import create_task_service, get_tasks_service, get_task_service, update_task_service, delete_task_service
from database import get_db
from schemas import TaskCreate, TaskUpdate, TaskResponse

app = FastAPI()


@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    return create_task_service(task)

@app.get("/tasks/", response_model=list[TaskResponse])
def get_tasks():
    return get_tasks_service()

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    return get_task_service(task_id)

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    return update_task_service(task_id, task_update)

@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    return delete_task_service(task_id)
