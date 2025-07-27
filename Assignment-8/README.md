# RAG Q&A Chatbot

A **Retrieval-Augmented Generation (RAG)** based chatbot that intelligently answers user queries by combining document retrieval with powerful generative language models (LLMs). This bot supports both **open-source models (e.g., Hugging Face)** and **proprietary models** (e.g., OpenAI GPT, Claude, Gemini, Groq) if free API access is available.

---

## What is RAG?

**RAG (Retrieval-Augmented Generation)** is a technique that retrieves relevant chunks from your own documents and feeds them into an LLM to generate factually grounded answers.

---
<img width="1046" height="810" alt="image" src="https://github.com/user-attachments/assets/7f0f86c8-76de-476d-8f3c-cff7e2d31b32" />

<img width="997" height="880" alt="image" src="https://github.com/user-attachments/assets/c6b1a14e-7293-4a72-9729-b524b396351d" />



## Features

-  Upload and parse documents (PDF etc.)
-  Chunking & semantic vector embedding
-  Vector-based similarity search (e.g., FAISS)
-  Conversational interface (Streamlit or Flask UI)
-  Uses LLMs (OpenAI GPT-4, Claude, Gemini, or Hugging Face)
-  RAG architecture for contextual Q&A
-  Environment variable-based API key handling (secure)

---

## Project Structure

