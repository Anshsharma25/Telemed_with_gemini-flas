# llm/llm.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # loads GOOGLE_API_KEY from your .env

llm = ChatGoogleGenerativeAI(
    temperature=0.7,
    model="gemini-1.5-flash",                  # correct model identifier
    api_key=os.getenv("GOOGLE_API_KEY")        # load your key from the env var
)

if __name__ == "__main__":
    print("👀 LLM is:", type(llm), llm)
