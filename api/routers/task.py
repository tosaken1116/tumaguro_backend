from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api.cruds.task import add_new_task, get_task_by_user_id
from api.db.database import get_db
from api.schema.task import GetTaskResult, PostTask, PostTaskResult
from api.utils.auth import get_current_user

task_router = APIRouter()

@task_router.post("/add",response_model=PostTaskResult)
async def add_task(payload:PostTask,db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    return add_new_task(db,payload.name,payload.dead_line,current_user.id)

@task_router.get("/my",response_model=GetTaskResult)
async def get_my_task(db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    return get_task_by_user_id(db,current_user.id)
