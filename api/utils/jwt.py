import os
from datetime import datetime, timedelta

import jwt

SECRET = os.environ.get('SECRET', 'jwt_secret')

def generate_token(id):
    exp_datetime = datetime.now()+ timedelta(10)
    jwt_payload = {
        "exp":exp_datetime,
        "id":id,
    }

    return jwt.encode(jwt_payload,SECRET,algorithm="HS256")

