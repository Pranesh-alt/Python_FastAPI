from fastapi import HTTPException, status
from uuid import UUID
from models import Task
from models import Task
from schemas import TaskCreate
from modules.users.validators import UserValidator
class TaskValidator:
    def validate_task(self,new_task: TaskCreate):
        if new_task.id is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task id cannot be None")
        self.validate_task_id(new_task.id)
        UserValidator().validate_user_id(user_id=(new_task.id))
    def validate_task_id(self,task_id: int):
        if not task_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task id" )
        task = Task.TaskDAO().find_by_id(task_id=task_id)
        if not task:
            raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found" )