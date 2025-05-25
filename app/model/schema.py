from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    user_name:str
    user_email:str
    user_phone:int
    user_password:str

class Login(BaseModel):
    user_email:str
    user_password:str   


class ItemSelection(BaseModel):
    model: str 
    item: str
  