
from fastapi import APIRouter, HTTPException, FastAPI, Depends
from sqlalchemy.orm import Session
from modules.users.services import create_user, all_user, find_user_by_id, find_user_by_email
from modules.users.schemas import UserCreate, UserResponse, UserUpdate



app =APIRouter()


# @app.post("/users/", response_model=UserResponse)
# def create_user(user: UserCreate, db: Session ):
#     return create_user(user)

# @app.get("/users/", response_model=list[UserResponse])
# def get_users():
#     db: Session = get_db()
#     return all_user(db)

# @app.get("/users/{user_id}", response_model=UserResponse)
# def get_user(user_id: int):
#     db: Session = get_db()
#     user = find_user_by_id(user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @app.put("/users/{user_id}", response_model=UserResponse)
# def update_user(user_id: int, user_update: UserUpdate):
#     db: Session = get_db()
#     user = update_user_service(user_id, user_update, db)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @app.delete("/users/{user_id}", response_model=dict)
# def delete_user_(user_id: int,response_model=dict):
#     return delete_user(user_id)