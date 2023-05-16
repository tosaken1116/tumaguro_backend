from fastapi import Depends, Security
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPException
from sqlalchemy.orm.session import Session

from api.cruds.user import get_user_by_id
from api.db.database import get_db
from api.utils.jwt import decode_token

security = HTTPBearer()
credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

def get_current_user(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        if credentials.scheme != 'Bearer':
            raise credentials_exception
        user_id = decode_token(credentials.credentials)["id"]
        return get_user_by_id(db,user_id)
    except Exception as e:
        print(e)
        raise credentials_exception
