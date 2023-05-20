from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import asc

from api.db.models import Task
from api.schema.task import DeleteTaskResult as DeleteSchema
from api.schema.task import Task as TaskSchema


def add_new_task(db,name:str,dead_line:str,user_id:str,comment:str)->TaskSchema:
    new_task = Task(name=name,dead_line=dead_line,user_id=user_id,comment=comment)
    db.add(new_task)
    db.commit()
    return TaskSchema.from_orm(new_task)

def get_task_by_user_id(db,user_id:str)->TaskSchema:
    task_orms = db.query(Task).filter(Task.user_id == user_id).order_by(asc(Task.dead_line)).all()
    tasks = []
    for task_orm in task_orms:
        tasks.append(TaskSchema.from_orm(task_orm))
    return {"tasks":tasks}

def delete_task_by_id(db,user_id:str,task_id:str)->DeleteSchema:
    delete_task_orm =db.query(Task).filter(Task.id == task_id).filter(Task.user_id==user_id).first()
    if delete_task_orm is None:
        raise HTTPException(status_code=404,detail="task not found")
    try:
        db.delete(delete_task_orm)
        db.commit()
        return {"status":"success"}
    except:
        raise HTTPException(status_code=500,detail="delete failed")

def update_task_by_id(db,user_id:str,task_id:str,name:str,dead_line:datetime,comment:str)->TaskSchema:
    update_task_orm = db.query(Task).filter(Task.id == task_id).filter(Task.user_id==user_id).first()
    if update_task_orm is None:
        raise HTTPException(status_code=404,detail="task not found")
    update_task_orm.name = name
    update_task_orm.dead_line = dead_line
    update_task_orm.comment = comment
    db.add(update_task_orm)
    db.commit()
    db.refresh(update_task_orm)
    return TaskSchema.from_orm(update_task_orm)