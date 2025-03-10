from sqlalchemy.orm import Session
from modules.Tasks.models import Task
from modules.Tasks.models import TaskCreate
from modules.Tasks.schemas import TaskUpdate
from fastapi import HTTPException,Depends
import uuid

task_dao = Task.TaskDAO() 

def create_task_service(task: TaskCreate, db: Session):
    return task_dao.create_task(task)

def get_tasks_service(task_id: int, db: Session):
    return task_dao.find_all()

def update_task_service(task_id: int, task_update: TaskUpdate, db: Session):
    task = task_dao.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return task

def delete_task_service(task_id: int, db: Session):
    task = task_dao.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
