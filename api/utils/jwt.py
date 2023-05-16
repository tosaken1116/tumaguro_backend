import os
from datetime import datetime, timedelta

import jwt

SECRET = os.environ.get('SECRET', 'jwt_secret')

def generate_token(user_id):
    exp_datetime = datetime.now()+ timedelta(days=10)
    jwt_payload = {
        "exp":exp_datetime,
        "id":user_id,
    }

    return jwt.encode(jwt_payload,SECRET,algorithm="HS256")

def decode_token(token:str):
    return jwt.decode(token, SECRET, algorithms=['HS256'])