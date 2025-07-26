from flask import Flask, request, render_template, session
import os
from vector_database import setup_vectorstore
from indexing import setup_llm
from loader import load_pdf_document
from chain_builder import create_qa_chain
from utils import handle_uploaded_file, format_chat_context

app = Flask(__name__)
app.secret_key = 'RAG_Working'

VECTORSTORE = None
QA_CHAIN = None

@app.route('/')
def index():
    session.clear()
    return render_template('chat.html')

@app.route('/upload', methods=['POST'])
def upload():
    global VECTORSTORE, QA_CHAIN
    file = request.files.get('document')
    if not file or file.filename == '':
        return render_template('chat.html', error="No file selected.")

    try:
        loader_type = request.form.get('loader_type', 'pypdf')
        temp_filename = handle_uploaded_file(file)
        docs = load_pdf_document(temp_filename, loader_type)
        os.unlink(temp_filename)

        VECTORSTORE = setup_vectorstore(docs)
        retriever = VECTORSTORE.as_retriever()
        llm = setup_llm()

        QA_CHAIN = create_qa_chain(llm, retriever)
        session['chat_history'] = []

        return render_template('chat.html', success="Document uploaded successfully! You can now start asking questions.")
    except Exception as e:
        return render_template('chat.html', error=f"Error processing document: {str(e)}")

@app.route('/ask', methods=['POST'])
def ask():
    global QA_CHAIN
    if QA_CHAIN is None:
        return render_template('chat.html', error="Please upload a document first.")

    question = request.form.get('question', '').strip()
    if not question:
        return render_template('chat.html', error="Please enter a question.")

    try:
        chat_history = session.get('chat_history', [])
        context_question = format_chat_context(chat_history, question)

        result = QA_CHAIN.invoke({"input": context_question})
        answer = result["answer"]

        chat_history.append({"human": question, "ai": answer})
        session['chat_history'] = chat_history

        return render_template('chat.html', chat_history=chat_history, success="Question answered successfully!")
    except Exception as e:
        return render_template('chat.html', error=f"Error processing question: {str(e)}")

@app.route('/clear', methods=['POST'])
def clear_chat():
    session['chat_history'] = []
    return render_template('chat.html', success="Chat history cleared.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
