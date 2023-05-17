from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api.cruds.user import create_new_user, signin as login, update_user_by_id
from api.utils.auth import get_current_user
from api.db.database import get_db
from api.schema.user import AuthInfo, SigninUser, SignupUser, User, UpdateUser


user_router = APIRouter()

@user_router.post("/signup",response_model=User)
async def signup(payload:SignupUser,db:Session =Depends(get_db)):
    return create_new_user(db,payload.email,payload.username,payload.password)

@user_router.post("/signin",response_model=AuthInfo)
async def signin(payload:SigninUser,db:Session =Depends(get_db)):
    return login(db,payload.email,payload.password)

@user_router.put("/me",response_model=User)
async def update_me(payload:UpdateUser,db:Session =Depends(get_db), current_user=Depends(get_current_user)):
    return update_user_by_id(db,current_user.id,payload.username)