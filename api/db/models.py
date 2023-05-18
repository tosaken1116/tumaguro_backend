from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
def gen_uuid():
    return str(uuid4())
class User(Base):
    __tablename__ = 'user'
    id = Column(String,primary_key=True,default=gen_uuid)
    email = Column(String,unique=True,nullable=False)
    username = Column(String,nullable=False)
    password_hash = Column(String,nullable=False)

class Task(Base):
    __tablename__ = 'task'
    id = Column(String,primary_key=True,default=gen_uuid)
    name = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.now().strftime('%x %X'))
    finished_at = Column(DateTime,nullable=True,default=None)
    dead_line = Column(DateTime,nullable=False)
    user_id = Column(String,nullable=False)

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(String,primary_key=True,default=gen_uuid)
    name = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.now().strftime('%x %X'))
    start_time = Column(DateTime,nullable=False)
    end_time = Column(DateTime,nullable=False)
    user_id = Column(String,nullable=False)