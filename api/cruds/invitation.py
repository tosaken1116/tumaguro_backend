from fastapi import HTTPException
from sqlalchemy import asc

from api.db.models import Invitation, Schedule, User
from api.schema.invitation import \
    GetInvitationResultOne as GetInvitationResultOneSchema
from api.schema.invitation import Invitation as InvitationSchema


def add_new_invitation(db,sender_email,recipient_email,schedule_id):
    schedule_exist = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if sender_email == recipient_email:
        raise HTTPException(status_code=403,detail="can't invite yourself")
    if schedule_exist is None:
        raise HTTPException(status_code=404,detail="schedule does not exist")
    user_exist = db.query(User).filter(User.email == recipient_email).first()
    if user_exist is None:
        raise HTTPException(status_code=404,detail="user does not exist")
    invitation_exist = db.query(Invitation).filter(Invitation.schedule_id == schedule_id).filter(Invitation.recipient_email == recipient_email).first()
    if invitation_exist is not None:
        raise HTTPException(status_code=403,detail="user already invited")
    new_invitation =Invitation(sender_email=sender_email,recipient_email=recipient_email,schedule_id=schedule_id)
    db.add(new_invitation)
    db.commit()
    db.refresh(new_invitation)
    return InvitationSchema.from_orm(new_invitation)

def get_invited_me(db,user_email):
    invitation_orms = db.query(Invitation).join(Schedule,Schedule.id==Invitation.schedule_id).filter(Invitation.recipient_email == user_email).order_by(asc(Invitation.created_at)).all()
    invitations = []
    for invitation_orm in invitation_orms:

        invitations.append(GetInvitationResultOneSchema.from_orm(invitation_orm))
    return {"invitations":invitations}

def get_my_inviting(db,user_email):
    invitation_orms = db.query(Invitation).join(Schedule,Schedule.id==Invitation.schedule_id).filter(Invitation.sender_email == user_email).order_by(asc(Invitation.created_at)).all()
    invitations = []
    for invitation_orm in invitation_orms:
        invitations.append(GetInvitationResultOneSchema.from_orm(invitation_orm))
    return {"invitations":invitations}

def invitation_reception(db,invitation_id:str,recipient_email:str,recipient_id:str,is_recept:bool):
    reception_invitation_orm = db.query(Invitation).filter(Invitation.id == invitation_id).first()
    if reception_invitation_orm is None:
        raise HTTPException(status_code=404,detail="invitation does not exist")
    if reception_invitation_orm.recipient_email != recipient_email:
        raise HTTPException(status_code=403,detail="you are not invited")
    if reception_invitation_orm.sender_email == recipient_email:
        raise HTTPException(status_code=403,detail="can't recept of your invitation")
    if reception_invitation_orm.is_recept is not None:
        raise HTTPException(status_code=403,detail="invitation is already received")
    reception_invitation_orm.is_recept = is_recept
    db.add(reception_invitation_orm)
    db.commit()
    db.refresh(reception_invitation_orm)
    if (is_recept):
        invited_schedule = db.query(Schedule).filter(Invitation.id == invitation_id).first()
        if invited_schedule is None:
            raise HTTPException(status_code=404,detail="invitation does not exist")
        new_schedule = new_schedule =Schedule(title=invited_schedule.title,start=invited_schedule.start,end=invited_schedule.end,user_id=recipient_id)
        db.add(new_schedule)
        db.commit()
        db.refresh(new_schedule)
    return {"status":"success"}

def delete_reception(db,invitation_id:str,sender_email:str):
    delete_invitation_orm = db.query(Invitation).filter(Invitation.id == invitation_id).first()
    if delete_invitation_orm is None:
        raise HTTPException(status_code=404,detail="invitation does not exist")
    if delete_invitation_orm.sender_email != sender_email:
        raise HTTPException(status_code=403,detail="this invitation sender is not you")
    try:
        db.delete(delete_invitation_orm)
        db.commit()
        return {"status":"success"}
    except:
        raise HTTPException(status_code=500,detail="delete failed")
