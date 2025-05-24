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

load_dotenv()
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.getenv('Google_credential')
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
app=FastAPI()
class ItemSelection(BaseModel):
    item: str
    model: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


app.include_router(router.router)
@app.post('/chatbot')
def chatbot(destination_file:str,source_file:UploadFile=File(...)):
    try:
        gcp_instance = gcp_st(destination_file,source_file)
        upload=gcp_instance.uploadtoGcs()
        return upload
    
    except Exception as err:
        print(err)    

@app.post("/chatprompt")
async def select_item(payload: ItemSelection):
    item = payload.item
    model = payload.model
    if str(model.strip())=='llama':
        answers=model_.groq_(item)
        app=[]
        for answer in answers:
            app.append(answer.choices[0].delta.content )

        app_filtered = [str(item) for item in app if item is not None]
        answer="".join(app_filtered)
        answer_json={"prompt":item,"answer":answer}
        encrypt=Encrpt.encrypt_(answer_json)
        db['llama'].insert_one(encrypt)
        return answer
    elif model.strip()=='gemini':
        answer=model_.goo_gemini(item)
        answer_json={"prompt":item,"answer":answer}
        encrypt=Encrpt.encrypt_(answer_json)
        db['gemini'].insert_one(encrypt)
        return answer
    else:
        print(model)
        return {"response": f"Unsupported model: {model}"}
    
        
