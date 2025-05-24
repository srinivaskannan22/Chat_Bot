from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import create_engine,or_,and_
from model.schema import User,Login
from database.database2 import get_db,engine
from model.model import UserModel,Base
from sqlalchemy.orm import Session
from response import Response



Base.metadata.create_all(engine)

router=APIRouter(tags=['Userprofile'])

@router.post('/user_create')
def createuser(user:User,db:Session=Depends(get_db)):
    user_=db.query(UserModel).filter(or_(UserModel.user_email == user.user_email,UserModel.user_phone == user.user_phone)).first()
    if user_ :
        raise HTTPException(status_code=409,detail='user already exist')
    us=UserModel(**user.dict())
    db.add(us)
    db.commit()
    return Response.upload_message('user create successfully')


@router.post('/login_authentication')
def login(login:Login,db: Session=Depends(get_db)):
    user_=db.query(UserModel).filter(and_(UserModel.user_email==login.user_email,UserModel.user_password==login.user_password))
    if user_:
        return Response.success_message('login successfull')
    else:
        raise HTTPException(status_code=401,detail='incorrect password')

    



