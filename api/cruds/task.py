from api.db.models import Task
from api.schema.task import PostTaskResult as TaskSchema


def add_new_task(db,name:str,dead_line:str):
    new_task = Task(name=name,dead_line=dead_line)
    db.add(new_task)
    db.commit()
    return TaskSchema.from_orm(new_task)
