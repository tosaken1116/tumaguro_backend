from pydantic import BaseModel
from datetime import datetime
class Schedule(BaseModel):
    id:str
    name:str
    start_time:datetime
    end_time:datetime
    created_at:datetime
    user_id:str
    class Config:
        orm_mode=True


class PostSchedule(BaseModel):
    name:str
    start_time:datetime
    end_time:datetime

class GetScheduleResult(BaseModel):
    schedules :list[Schedule]
