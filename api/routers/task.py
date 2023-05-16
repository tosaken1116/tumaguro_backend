from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from api.utils.auth import get_current_user
from api.cruds.task import add_new_task
from api.db.database import get_db
from api.schema.task import PostTask, PostTaskResult

task_router = APIRouter()

@task_router.post("/add",response_model=PostTaskResult)
async def add_task(payload:PostTask,db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    return add_new_task(db,payload.name,payload.dead_line)