from storage.storage import gcp_st
from service.chat_service import model_
from dotenv import load_dotenv
from fastapi import FastAPI,File,UploadFile,APIRouter,HTTPException,Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database.database import db
from service.encrypt_service import Encrpt
from model.schema import ItemSelection
from passlib.context import CryptContext
from service.auth import get_current_user
load_dotenv()

router2=APIRouter(tags=['Chat_Ai'])

@router2.post('/chatbot')
def chatbot(destination_file:str,source_file:UploadFile=File(...)):
    try:
        gcp_instance = gcp_st(destination_file,source_file)
        upload=gcp_instance.uploadtoGcs()
        return upload
    
    except Exception as err:
        print(err)    

@router2.post("/chatprompt")
async def select_item(request:Request,payload: ItemSelection):
    item = payload.item
    model = payload.model
    try:
        a=get_current_user(request)
        user_id=a['user_id']    
        if str(model.strip())=='llama':
            answers=model_.groq_(item)
            app=[]
            for answer in answers:
                app.append(answer.choices[0].delta.content )

            app_filtered = [str(item) for item in app if item is not None]
            answer="".join(app_filtered)
            answer_json={"user_id":user_id,"prompt":item,"answer":answer}
            encrypt=Encrpt.encrypt_(answer_json)
            db['llama'].insert_one(encrypt)
            return answer
        elif model.strip()=='gemini':
            answer=model_.goo_gemini(item)
            answer_json={"user_id":user_id,"prompt":item,"answer":answer}
            encrypt=Encrpt.encrypt_(answer_json)
            db['gemini'].insert_one(encrypt)
            return answer
        else:
            raise HTTPException(status_code=405,detail='service not support ')
    except :
        raise HTTPException(status_code=404,detail='unautherized')
        