from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    comment = Column(String)

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(String,primary_key=True,default=gen_uuid)
    name = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.now().strftime('%x %X'))
    start = Column(DateTime,nullable=False)
    end = Column(DateTime,nullable=False)
    user_id = Column(String,nullable=False)
    invitation = relationship("Invitation", foreign_keys="Invitation.schedule_id")
    comment = Column(String)

class Invitation(Base):
    __tablename__ = 'invitations'
    id = Column(String,primary_key=True,default=gen_uuid)
    created_at = Column(DateTime,default=datetime.now().strftime('%x %X'))
    schedule_id = Column(String,ForeignKey("schedule.id"))
    sender_email = Column(String,nullable=False)
    recipient_email = Column(String,nullable=False)
    deleted_at = Column(String,default=None)
    is_recept = Column(Boolean,default=None)

    schedule =  relationship("Schedule", back_populates="invitation")
