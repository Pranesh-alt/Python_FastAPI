from utils.database import Session,engine
from sqlmodel import SQLModel,Field
from uuid import UUID,uuid4
from sqlmodel import select
from datetime import datetime,timezone
from typing import Optional


def generate_time_stamp():
    return datetime.now(timezone.utc)





class TaskCreate(SQLModel):
    description: Optional[str] = None
    completed: bool = False
    user_id: int


class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    id: int = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str = Field(nullable=True)
    completed: bool = Field(default=False)
    user_id: int = Field(foreign_key="user.id")
    
    
    class TaskDAO:
        def create_task(self, new_task: TaskCreate):
            with Session(engine) as session:
                db_task = Task(**new_task.model_dump())
                session.add(db_task)
                session.commit()
                session.refresh(db_task)
            return db_task
        def find_all(self):
            with Session(engine) as session:
                tasks = session.exec(select(Task)).all()
            return tasks
        def find_by_id(self, task_id:int):
            with Session(engine) as session:
                task = session.exec(select(Task).where(Task.id == task_id)).first()
            return task
        def find_by_user_id(self, user_id: int):
            with Session(engine) as session:
                task = session.exec(select(Task).where(Task.user_id == user_id)).all()
            return task
__all__ = ["generate_timestamp", "Task", "TaskBase", "TaskDAO"]
    
    