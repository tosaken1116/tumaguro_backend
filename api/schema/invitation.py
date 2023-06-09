from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from api.schema.schedule import Schedule


class Invitation(BaseModel):
    id:str
    created_at:datetime
    recipient_email:str
    class Config:
        orm_mode=True

class PostInvitation(BaseModel):
    recipient_email:str
    schedule_id:str

class GetInvitationResultOne(BaseModel):
    created_at:datetime
    id:str
    sender_email:str
    is_recept:Optional[bool]
    recipient_email:str
    schedule:Schedule
    class Config:
        orm_mode=True

class GetInvitationResult(BaseModel):
    invitations :list[GetInvitationResultOne]

class ReceptInvitation(BaseModel):
    is_recept:bool
class ReceptInvitationResult(BaseModel):
    status:str
class DeleteInvitationResult(BaseModel):
    status:str
