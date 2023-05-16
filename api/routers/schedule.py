from fastapi import APIRouter,Depends
from api.schema.schedule import PostSchedule
from api.utils.auth import get_current_user
from sqlalchemy.orm.session import Session
from api.db.database import get_db
from api.cruds.schedule import add_new_schedule
from api.schema.schedule import Schedule
schedule_router = APIRouter()

@schedule_router.post("/add",response_model=Schedule)
async def add_schedule(payload:PostSchedule,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return add_new_schedule(db,payload.name,payload.start_time,payload.end_time,current_user.id)