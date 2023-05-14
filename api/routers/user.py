from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api.cruds.user import create_new_user
from api.db.database import get_db
from api.schema.user import SignupUser, User

user_router = APIRouter()

@user_router.post("/signup",response_model=User)
async def signup(payload:SignupUser,db:Session =Depends(get_db)):
    return create_new_user(db,payload.email,payload.username,payload.password)