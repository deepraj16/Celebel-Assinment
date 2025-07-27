from langchain_community.vectorstores import FAISS
from langchain_mistralai.embeddings import MistralAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

def setup_vectorstore(docs):
    """Setup and return the vector store"""
    embeddings = MistralAIEmbeddings(
   # api_key="",  // api key in evn  
    model="mistral-embed",                      
    )
    return FAISS.from_documents(docs, embeddings)
