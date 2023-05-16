import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String,primary_key=True,default=str(uuid.uuid4()))
    email = Column(String,unique=True,nullable=False)
    username = Column(String,nullable=False)
    password_hash = Column(String,nullable=False)

class Task(Base):
    __tablename__ = 'task'
    id = Column(String,primary_key=True,default=str(uuid.uuid4()))
    name = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.now().strftime('%x %X'))
    finished_at = Column(DateTime,nullable=True,default=None)
    dead_line = Column(DateTime,nullable=False)

