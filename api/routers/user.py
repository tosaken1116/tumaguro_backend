from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api.cruds.user import create_new_user, signin as login
from api.db.database import get_db
from api.schema.user import AuthInfo, SigninUser, SignupUser, User

user_router = APIRouter()

@user_router.post("/signup",response_model=User)
async def signup(payload:SignupUser,db:Session =Depends(get_db)):
    return create_new_user(db,payload.email,payload.username,payload.password)

@user_router.post("/signin",response_model=AuthInfo)
async def signin(payload:SigninUser,db:Session =Depends(get_db)):
    return login(db,payload.email,payload.password)
