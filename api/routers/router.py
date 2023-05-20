from fastapi import APIRouter

from api.routers.invitation import invitation_router
from api.routers.schedule import schedule_router
from api.routers.task import task_router
from api.routers.user import user_router

router = APIRouter()

router.include_router(user_router,prefix="/users",tags=["users"])
router.include_router(task_router,prefix="/task",tags=["task"])
router.include_router(schedule_router,prefix="/schedule",tags=["schedule"])
router.include_router(invitation_router,prefix="/invitation",tags=["invitation"])