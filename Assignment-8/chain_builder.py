from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def create_qa_chain(llm, retriever):
    system_prompt = (
        "You are a helpful AI assistant. Use the following pieces of retrieved context "
        "to answer the question. If you don't know the answer, say that you don't know. "
        "Keep the answer concise and relevant to the context provided.\n\n"
        "Context: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)
