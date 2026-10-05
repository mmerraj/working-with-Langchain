from fastapi import FastAPI
from pydantic import BaseModel
from os import getenv
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import warnings

load_dotenv()

warnings.filterwarnings(
    "ignore",
    message="Direct use of *"
)
api_key = getenv("google_api_key")

class Queryai(BaseModel):
    question: str

app = FastAPI()


llm = GoogleGenerativeAI(model="gemini-3.8-flash", google_api_key=api_key)



@app.post("/ask-ai")
def ask_ai(data: Queryai):
    answer = llm.invoke(data.question)

    return{
        "answer":answer
    }
 
