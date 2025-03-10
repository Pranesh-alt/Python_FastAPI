from .models import UserBase, User, UserCreate
from utils.database import Session, engine
from .models import UserDAO  
from sqlmodel import select



user_dao=UserDAO()


def create_user(new_user: UserCreate):
    return user_dao.create_user(new_user)



def all_user():
    return user_dao.find_all()


def find_user_by_id(user_id:int):
    return user_dao.find_by_id(user_id)


def find_user_by_email(email:str):
    return user_dao.find_by_email(email)


__all__=["create_user","all_user","find_user_by_id","find_user_by_email"]