import os
from app.storage.storage import gcp_st
from app.storage.model import model_
from dotenv import load_dotenv
from fastapi import FastAPI,File,UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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
        print(app_filtered)
        return "".join(app_filtered)
    elif model.strip()=='gemini':
        answer=model_.goo_gemini(item)
        return answer
    
        
