from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    id:str
    title:str
    finished_at:Optional[datetime]
    created_at:datetime
    dead_line:datetime
    user_id:str
    comment:str
    class Config:
        orm_mode=True

class PostTask(BaseModel):
    title:str
    dead_line:datetime
    comment:str


class GetTaskResult(BaseModel):
    tasks:list[Task]
class DeleteTaskResult(BaseModel):
    status:str
