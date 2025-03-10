from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(TaskCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True  
