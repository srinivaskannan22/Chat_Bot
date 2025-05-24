from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String

Base=declarative_base()
class UserModel(Base):
    __tablename__='user'
    user_id=Column(Integer,primary_key=True,autoincrement=True)
    user_name=Column(String)
    user_email=Column(String)
    user_phone=Column(Integer)
    user_password=Column(String)