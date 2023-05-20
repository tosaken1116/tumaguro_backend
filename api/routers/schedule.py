from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api.cruds.schedule import (add_new_schedule, delete_schedule_by_id,
                                get_schedule_by_user_id, update_schedule_by_id)
from api.db.database import get_db
from api.schema.schedule import (DeleteScheduleResult, GetScheduleResult,
                                 PostSchedule, Schedule)
from api.utils.auth import get_current_user

schedule_router = APIRouter()

@schedule_router.post("/add",response_model=Schedule)
async def add_schedule(payload:PostSchedule,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return add_new_schedule(db,payload.name,payload.start_time,payload.end_time,payload.comment,current_user.id)
@schedule_router.get("/my",response_model=GetScheduleResult)
async def get_my_schedule(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return get_schedule_by_user_id(db,current_user.id)
@schedule_router.delete("/{schedule_id}",response_model=DeleteScheduleResult)
async def delete_schedule_one(schedule_id:str,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return delete_schedule_by_id(db,schedule_id,current_user.id)
@schedule_router.put("/{schedule_id}",response_model=Schedule)
async def update_schedule_one(schedule_id:str,payload:PostSchedule,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return update_schedule_by_id(db,schedule_id,current_user.id,payload.name,payload.start_time,payload.end_time,payload.comment)