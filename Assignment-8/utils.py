import tempfile
def handle_uploaded_file(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(file.read())
        return temp_file.name

def format_chat_context(chat_history, question):
    if not chat_history:
        return question
    recent_history = chat_history[-3:]
    history_context = "\n".join([
        f"Previous Q: {entry['human']}\nPrevious A: {entry['ai']}"
        for entry in recent_history
    ])
    return f"Chat History:\n{history_context}\n\nCurrent Question: {question}"
