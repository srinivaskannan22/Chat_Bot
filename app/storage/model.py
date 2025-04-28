from groq import Groq
import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/Users/bootlabs/genai_practice/copper-triumph-457514-u3-eabe6b5b545b.json'

client = Groq()

class model_:
    def groq_(content):
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": str(content)}],
            temperature=0.2,
            max_completion_tokens=8000,
            top_p=0.95,
            stream=True,
            stop=None,
        )

        return completion
    
    def goo_gemini(content):
        client = genai.Client(
        vertexai=True, project="copper-triumph-457514-u3", location="us-east1"
        )
        chat = client.chats.create(model="gemini-1.5-flash-002")
        response = chat.send_message(str(content))
        return(response.text)

