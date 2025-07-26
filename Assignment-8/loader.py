from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf_document(file_path, loader_type="pypdf"):
    """Load PDF document using different loaders"""
    try:    
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        splits = text_splitter.split_documents(docs)
        return splits
    
    except Exception as e:
        raise Exception(f"Error loading PDF with {loader_type}: {str(e)}")
