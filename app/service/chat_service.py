from groq import Groq
import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
from database.database import db
from fastapi import Request,HTTPException
from .encrypt_service import Encrpt
from .auth import get_current_user

load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/Users/bootlabs/genai_practice/copper-triumph-457514-u3-eabe6b5b545b.json'

client = Groq()
Encrypt=Encrpt()

class model_:

    def ___init__(self):
        self.llama=True

    def database(self,request: Request):
        try:
            user=get_current_user(request)
            user_id=user['user_id']
            model="llama" if self.llama else "gemini"
            if user_id:
                datas=db[model].find({"user_id":user_id}) 
                result=[]
                for data in datas:
                    data_=Encrpt.decrypt_(data)
                    result.append(data_)
                    print(result)
                return result    
        except Exception as error :
               raise HTTPException(status_code=400,detail='error due to {error}')
    
    def groq_(self,content,request: Request):
        self.llama=True
        database=self.database(request)
        prompt = f"""
                Here is the user's question: "{content}"

                Check the following interaction history: {database}

                If the same question was already asked by the user, return the previous answer.

                If not, generate a fresh response — but ONLY return the final answer text. 
                Do not include any explanation, reasoning, or metadata. Respond like a human assistant would.

                Question: "{content}"
                """
        
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": str(prompt)}],
            temperature=0.2,
            max_completion_tokens=8000,
            top_p=0.95,
            stream=True,
            stop=None,
        )

        return completion
    
    def goo_gemini(self,content,request: Request):
        self.llama=False
        database=self.database(request)
        prompt = f"""
                Here is the user's question: "{content}"

                Check the following interaction history: {database}

                If the same question was already asked by the user, return the previous answer.

                If not, generate a fresh response — but ONLY return the final answer text. 
                Do not include any explanation, reasoning, or metadata. Respond like a human assistant would.

                Question: "{content}"
                """
        
        client = genai.Client(
        vertexai=True, project="copper-triumph-457514-u3", location="us-east1"
        )
        chat = client.chats.create(model="gemini-1.5-flash-002")
        response = chat.send_message(prompt)
        return(response.text)

