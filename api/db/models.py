import uuid

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String,primary_key=True,default=str(uuid.uuid4()))
    email = Column(String,unique=True,nullable=False)
    username = Column(String,nullable=False)
    password_hash = Column(String,nullable=False)