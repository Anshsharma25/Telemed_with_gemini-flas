import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY",
    "AIzaSyCgmE3ddkfMGP3bbNaakAHjwYVSlEHFAMs"
)

llm = ChatGoogleGenerativeAI(
    temperature=0.7,
    model="gemini-1.5-flash",
    api_key=GOOGLE_API_KEY
)

if __name__ == "__main__":
    print("👀 LLM is:", type(llm), llm)
