# llm/llm.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    temperature=0.7,
    model="gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")    # use the correct kwarg name: `api_key`
)

print("👀 LLM is:", type(llm), llm)  # should show ChatGoogleGenerativeAI
