import os
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import warnings

load_dotenv()

warnings.filterwarnings(
    "ignore",
    message="Direct use of automatic function calling (AFC) in Models.generate_content is not recommended.*"
)
api_key = os.getenv("google_api_key")



llm = GoogleGenerativeAI(model="gemini-3.8-flash", google_api_key=api_key)
print(
     llm.invoke(
         "What are some of the pros and cons of Python as a programming language? in one sentence"
     )
)

