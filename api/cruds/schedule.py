from fastapi import HTTPException
from sqlalchemy import asc

from api.db.models import Schedule
from api.schema.schedule import Schedule as ScheduleSchema


def add_new_schedule(db,title,start,end,comment,user_id):
    new_schedule =Schedule(title=title,start=start,end=end,user_id=user_id,comment=comment)
    db.add(new_schedule)
    db.commit()
    return ScheduleSchema.from_orm(new_schedule)
def get_schedule_by_user_id(db,user_id):
    schedule_orms = db.query(Schedule).filter(Schedule.user_id == user_id).order_by(asc(Schedule.start)).all()
    schedules = []
    for schedule_orm in schedule_orms:
        schedules.append(ScheduleSchema.from_orm(schedule_orm))
    return {"schedules":schedules}

def delete_schedule_by_id(db,schedule_id,user_id):
    delete_schedule_orm = db.query(Schedule).filter(Schedule.id == schedule_id).filter(Schedule.user_id == user_id).first()
    if delete_schedule_orm is None:
        raise HTTPException(status_code=404,detail="schedule does not exist")
    try:
        db.delete(delete_schedule_orm)
        db.commit()
        return {"status":"success"}
    except:
        raise HTTPException(status_code=500,detail="delete failed")

def update_schedule_by_id(db,schedule_id,user_id,title,start,end,comment):
    update_schedule_orm = db.query(Schedule).filter(Schedule.id == schedule_id).filter(Schedule.user_id == user_id).first()
    if update_schedule_orm is None:
        raise HTTPException(status_code=404,detail="schedule does not exist")
    update_schedule_orm.title = title
    update_schedule_orm.start = start
    update_schedule_orm.end = end
    update_schedule_orm.comment = comment
    db.add(update_schedule_orm)
    db.commit()
    db.refresh(update_schedule_orm)
    return ScheduleSchema.from_orm(update_schedule_orm)