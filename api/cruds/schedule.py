from api.db.models import Schedule
from api.schema.schedule import Schedule as ScheduleSchema


def add_new_schedule(db,name,start_time,end_time,user_id):
    new_schedule =Schedule(name=name,start_time=start_time,end_time=end_time,user_id=user_id)
    db.add(new_schedule)
    db.commit()
    return ScheduleSchema.from_orm(new_schedule)
def get_schedule_by_user_id(db,user_id):
    schedule_orms = db.query(Schedule).filter(Schedule.user_id == user_id).all()
    schedules = []
    for schedule_orm in schedule_orms:
        schedules.append(ScheduleSchema.from_orm(schedule_orm))
    return {"schedules":schedules}