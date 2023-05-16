from pydantic import BaseModel

class Task(BaseModel):
    id:str
    name:str
    finished_at:str
    created_at:str
    dead_line:str

class PostTask(BaseModel):
    name:str
    dead_line:str

class PostTaskResult(BaseModel):
    name:str
    class Config:
        orm_mode=True
