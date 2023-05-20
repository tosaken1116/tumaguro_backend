from pydantic import BaseModel
from datetime import datetime
class Schedule(BaseModel):
    id:str
    name:str
    start:datetime
    end:datetime
    created_at:datetime
    user_id:str
    comment:str
    class Config:
        orm_mode=True


class PostSchedule(BaseModel):
    name:str
    start:datetime
    end:datetime
    comment:str

class GetScheduleResult(BaseModel):
    schedules :list[Schedule]

class DeleteScheduleResult(BaseModel):
    status:str
