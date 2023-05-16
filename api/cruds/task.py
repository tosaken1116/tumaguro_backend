from datetime import datetime

from api.db.models import Task
from api.schema.task import GetTaskResult as GetSchema
from api.schema.task import Task as TaskSchema
from api.schema.task import PostTaskResult as PostSchema


def add_new_task(db,name:str,dead_line:str,user_id:str):
    new_task = Task(name=name,dead_line=dead_line,user_id=user_id)
    db.add(new_task)
    db.commit()
    return PostSchema.from_orm(new_task)

def get_task_by_user_id(db,user_id):
    print("================================")
    task_orms = db.query(Task).filter(Task.user_id == user_id).all()
    print("================================")
    tasks = []
    for task_orm in task_orms:
        tasks.append(TaskSchema.from_orm(task_orm))
    print("================================")
    print(tasks)
    return {"tasks":tasks}