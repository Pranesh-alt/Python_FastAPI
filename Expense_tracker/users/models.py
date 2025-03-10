from utils.database import Session,engine
from sqlmodel import SQLModel, Field
from uuid import UUID,uuid4
from datetime import datetime,timezone
from sqlmodel import select


def generate_time_stamp():
    return datetime.now(timezone.utc)

class UserBase(SQLModel):
    full_name:str=Field(min_length=3)
    email:str=Field(unique=True)
    
    
class User(UserBase,table=True):  
    id:int= Field(primary_key=True)
    created_at:datetime=Field(generate_time_stamp)
    updated_at:datetime=Field(generate_time_stamp)
    
class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserUpdate(SQLModel):
    full_name: str = Field(min_length=3, default=None)
    email: str = Field(unique=True, default=None)
    password: str = Field(min_length=8, default=None)

class UserDAO:
    def create_user(self, new_user: UserCreate):
        with Session(engine) as session:
            db_user = User(**new_user.model_dump())
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
        return db_user

    def find_all(self):
        with Session(engine) as session:
            users = session.exec(select(User)).all()
        return users

    def find_by_id(self, user_id: int):
        with Session(engine) as session:
            user = session.exec(select(User).where(User.id == user_id)).first()
        return user

    def find_by_email(self, email: str):
        with Session(engine) as session:
            user = session.exec(select(User).where(User.email == email)).first()
        return user
   
    def update_user(self, user_id: int, user_update: UserUpdate):
        with Session(engine) as session:
            user = self.find_by_id(user_id)
            if not user:
                return None
            update_data = user_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(user,key,value)
                session.commit()
                session.refresh(user)
            return user
    def delete_user(self, user_id:int):
        with Session(engine) as session:
            user = self.find_by_id(user_id)
            if not user:
                return None
            session.delete(user)
            session.commit()
            session.refresh(user)
            
__all__=["UserBase", "User"]