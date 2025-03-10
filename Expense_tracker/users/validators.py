from fastapi import HTTPException, status
from uuid import UUID
from modules.users.models import UserDAO  

class UserValidator:
    def validate_user_id(self, user_id: int):
        if not user_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        user = UserDAO().find_by_id(user_id=user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User Not Found"
            )
