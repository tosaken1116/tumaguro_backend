from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api.cruds.invitation import (add_new_invitation, delete_reception,
                                  get_invited_me, get_my_inviting,
                                  invitation_reception)
from api.db.database import get_db
from api.schema.invitation import (DeleteInvitationResult, GetInvitationResult,
                                   Invitation, PostInvitation,
                                   ReceptInvitation, ReceptInvitationResult)
from api.utils.auth import get_current_user

invitation_router = APIRouter()

@invitation_router.post("/add",response_model=Invitation)
async def add_invitation(payload:PostInvitation,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return add_new_invitation(db,current_user.email,payload.recipient_email,payload.schedule_id)

@invitation_router.post("/recept/{invitation_id}",response_model=ReceptInvitationResult)
async def recept_inviting(invitation_id:str,payload:ReceptInvitation,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return invitation_reception(db,invitation_id,current_user.email,current_user.id,payload.is_recept)

@invitation_router.get("/me/invited",response_model=GetInvitationResult)
async def get_user_inviting_me(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return get_invited_me(db,current_user.email)

@invitation_router.get("/me/inviting",response_model=GetInvitationResult)
# @invitation_router.get("/me/inviting")
async def get_my_inviting_users(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return get_my_inviting(db,current_user.email)

@invitation_router.delete("/{invitation_id}",response_model=DeleteInvitationResult)
async def delete_inviting_one(invitation_id:str,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return delete_reception(db,invitation_id,current_user.email)
