from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime,timedelta
from fastapi import HTTPException
from fastapi.requests import Request
from model.model import UserModel

with open("secret.key","rb") as file:
    secret_key=file.read()

SESSION_COOKIE_NAME = "session_token"

def create_token(data:dict):
    to_encode=data.copy()
    to_encode['time'] = (datetime.utcnow() + timedelta(minutes=30)).isoformat()
    encode=jwt.encode(to_encode,secret_key,algorithm="HS256")
    return encode


def verify_token(token:str,credential_exception):
    try:
        decode=jwt.decode(token,secret_key,algorithms=["HS256"])
        email_id:str=decode.get('user.email_id')
        if email_id is None:
            raise credential_exception
        token_data=UserModel(email_id=email_id)
        return token_data
    except JWTError:
        return credential_exception    

def get_current_user(request:Request):
    token = request.cookies.get(SESSION_COOKIE_NAME)
    credential_exception = HTTPException(status_code=401, detail="Could not validate credentials")  
    return verify_token(token, credential_exception)