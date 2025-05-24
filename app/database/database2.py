from sqlalchemy.orm import Session,sessionmaker,declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

Base=declarative_base()

engine=create_engine(os.getenv('DATABASE_CONNECTION_URI'))

sessionlocal=sessionmaker(bind=engine,class_=Session)


def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()   