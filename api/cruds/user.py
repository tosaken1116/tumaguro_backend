import hashlib

from fastapi import HTTPException

from api.db.models import User
from api.schema.user import User as UserSchema


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
