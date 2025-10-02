import dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

global llm

llm = None

def get_or_create_llm():
    global llm
    if llm is None:
        dotenv.load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        model=os.getenv('GEMINI_MODEL')
        llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key)
    return llm




