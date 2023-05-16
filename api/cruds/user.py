import hashlib

from fastapi import HTTPException

from api.db.models import User
from api.schema.user import User as UserSchema
from api.utils.jwt import generate_token

def gen_password_hash(password: str):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def create_new_user(db,email:str,username:str,password:str):
    user =db.query(User).filter(User.email == email).first()
    if user is not None:
        raise HTTPException(status_code=409,detail="email already in use")
    new_user = User(email=email,username=username,password_hash=gen_password_hash(password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserSchema.from_orm(new_user)

def signin(db,email:str,password:str):
    user =db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=400,detail="user does not exist")
    if user.password_hash != gen_password_hash(password):
        raise HTTPException(status_code=403,detail="password is incorrect")
    return generate_token(user.id)

def get_user_by_id(db,id:str):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=400,detail="user does not exist")
    return user