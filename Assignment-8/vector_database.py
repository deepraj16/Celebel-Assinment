from langchain_community.vectorstores import FAISS
from langchain_mistralai.embeddings import MistralAIEmbeddings

def setup_vectorstore(docs):
    """Setup and return the vector store"""
    embeddings = MistralAIEmbeddings(
    api_key="lHcwga2vJ6yyjV470WdMIFn5hRgtMbcc",  
    model="mistral-embed",                      
    )
    return FAISS.from_documents(docs, embeddings)