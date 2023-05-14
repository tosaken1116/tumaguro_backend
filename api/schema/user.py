from pydantic import BaseModel


class User(BaseModel):
    id:str
    email:str
    username:str
    class Config:
        orm_mode=True

class SignupUser(BaseModel):
    email:str
    username:str
    password:str