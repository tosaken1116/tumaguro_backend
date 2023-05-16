from api.db.models import Schedule
from api.schema.schedule import Schedule as ScheduleSchema


def add_new_schedule(db,name,start_time,end_time,user_id):
    new_schedule =Schedule(name=name,start_time=start_time,end_time=end_time,user_id=user_id)
    db.add(new_schedule)
    db.commit()
    return ScheduleSchema.from_orm(new_schedule)
