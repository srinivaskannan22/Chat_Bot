from fastapi import APIRouter,Depends,HTTPException,Response,Request
from sqlalchemy import create_engine,or_,and_
from model.schema import User,Login
from database.database2 import get_db,engine
from model.model import UserModel,Base
from sqlalchemy.orm import Session
from response import Response_
from service import auth
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from passlib.context import CryptContext
from fastapi.responses import RedirectResponse
from service.auth import get_current_user

Base.metadata.create_all(engine)

pwdcontext=CryptContext(schemes=['bcrypt'],deprecated='auto')

router=APIRouter(tags=['User_Profile'])

SESSION_COOKIE_NAME = "session_token"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login_authentication")

def checking_password(a,b):
    return pwdcontext.verify(a,b)

@router.post('/user_create')
def createuser(user:User,db:Session=Depends(get_db)):
    hashpassword=pwdcontext.hash(user.user_password)
    user.user_password=hashpassword
    user_=db.query(UserModel).filter(or_(UserModel.user_email == user.user_email,UserModel.user_phone == user.user_phone)).first()
    if user_ :
        raise HTTPException(status_code=409,detail='user already exist')
    us=UserModel(**user.dict())
    db.add(us)
    db.commit()
    return Response_.upload_message('user create successfully')


@router.post('/login_authentication')
def login(response:Response,login:OAuth2PasswordRequestForm=Depends(),db: Session=Depends(get_db)):
    user_=db.query(UserModel).filter(UserModel.user_email==login.username).first()
    if not user_:
        raise HTTPException(status_code=404,detail='user not found')
    if not checking_password(login.password,user_.user_password):
        raise HTTPException(status_code=401,detail='Password incorrect')
    jwt_encode=auth.create_token(({"user_id":user_.user_id,"user.email_id":login.username}))
    response.set_cookie(key=SESSION_COOKIE_NAME,value=jwt_encode,httponly=True,secure=True,expires=1800)
    response.headers['Autherisation']=(jwt_encode)
    return Response_.success_message('login successfull')    
    
@router.get("/logout")
async def logout(response:Response):
    response.delete_cookie(key=SESSION_COOKIE_NAME)
    return Response_.success_message('logout successsfully')

@router.put('/updatepassword')
async def updata_password(password:str,response: Request,db: Session=Depends(get_db)):
    try:
        user=get_current_user(response)
        if user:
            data=db.query(UserModel).filter(UserModel.user_email==user["user.email_id"]).first()
            hashpassword=pwdcontext.hash(password)
            data.user_password=hashpassword
            db.commit()
            return RedirectResponse(url="/logout",status_code=303)
        else:
            pass

    except Exception as err:
        print(err)    
    



    



