from datetime import datetime

from fastapi import HTTPException

from api.db.models import Task
from api.schema.task import GetTaskResult as GetSchema
from api.schema.task import PostTaskResult as PostSchema
from api.schema.task import Task as TaskSchema


def add_new_task(db,name:str,dead_line:str,user_id:str):
    new_task = Task(name=name,dead_line=dead_line,user_id=user_id)
    db.add(new_task)
    db.commit()
    return PostSchema.from_orm(new_task)

def get_task_by_user_id(db,user_id):
    task_orms = db.query(Task).filter(Task.user_id == user_id).all()
    tasks = []
    for task_orm in task_orms:
        tasks.append(TaskSchema.from_orm(task_orm))
    return {"tasks":tasks}

def delete_task_by_id(db,user_id,task_id):
        delete_task_orm =db.query(Task).filter(Task.id == task_id).filter(Task.user_id==user_id).first()
        if delete_task_orm is None:
            raise HTTPException(status_code=404,detail="task not found")
        try:
            db.delete(delete_task_orm)
            db.commit()
            return {"status":"success"}
        except:
            raise HTTPException(status_code=500,detail="delete failed")