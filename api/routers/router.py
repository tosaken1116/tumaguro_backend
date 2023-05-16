from fastapi import APIRouter

from api.routers.task import task_router
from api.routers.user import user_router

router = APIRouter()

router.include_router(user_router,prefix="/users",tags=["users"])
router.include_router(task_router,prefix="/task",tags=["task"])