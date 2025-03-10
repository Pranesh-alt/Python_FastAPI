from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int


class UserUpdate(UserBase):
    pass


