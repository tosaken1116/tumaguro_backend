from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api.cruds.task import (add_new_task, delete_task_by_id,
                            get_task_by_user_id, update_task_by_id)
from api.db.database import get_db
from api.schema.task import DeleteTaskResult, GetTaskResult, PostTask, Task
from api.utils.auth import get_current_user

task_router = APIRouter()

@task_router.post("/add",response_model=Task)
async def add_task(payload:PostTask,db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    return add_new_task(db,payload.title,payload.dead_line,current_user.id,payload.comment)

@task_router.get("/my",response_model=GetTaskResult)
async def get_my_task(db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    return get_task_by_user_id(db,current_user.id)

@task_router.delete("/{task_id}",response_model=DeleteTaskResult)
async def delete_task_one(task_id:str, db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    return delete_task_by_id(db,current_user.id,task_id)

@task_router.put("/{task_id}",response_model=Task)
async def update_task_one(task_id:str,payload:PostTask, db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    return update_task_by_id(db,current_user.id,task_id,payload.title,payload.dead_line,payload.comment)