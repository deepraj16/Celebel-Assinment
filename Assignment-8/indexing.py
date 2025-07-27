from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

def setup_llm():
    """Setup and return the LLM model"""
    llm = ChatMistralAI()
    return llm

