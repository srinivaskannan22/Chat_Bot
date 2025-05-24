import os
from storage.storage import gcp_st
from service.chat_service import model_
from dotenv import load_dotenv
from fastapi import FastAPI,File,UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database.database import db
from service.encrypt_service import Encrpt
from router import router
from router import chatrouter

load_dotenv()
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.getenv('Google_credential')
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


app.include_router(router.router)
app.include_router(chatrouter.router2)