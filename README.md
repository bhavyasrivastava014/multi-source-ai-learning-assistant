# Multi-Source AI Learning Assistant

## Overview

The *Multi-Source AI Learning Assistant* is a full-stack AI application built for the *Samasocial Technical Assignment*.

It implements both required tasks:

### *Task 1 – Multi-Source RAG Chatbot*

An AI assistant that ingests content from *PDFs, PPTX presentations, webpages, and YouTube videos, indexes it using semantic embeddings, and answers questions with **Retrieval-Augmented Generation (RAG)* and *source citations*.

### *Task 2 – Conversational AI Course Planner*

A mentor-focused assistant that creates structured course plans through multi-turn conversations and allows iterative refinement using natural language.

---

## Features

### 📚 Multi-Source Learning Assistant

* Upload and chat with *PDF documents*
* Upload and chat with *PPTX presentations*
* Extract and index *webpage content*
* Extract and index *YouTube transcripts*
* Combine multiple sources in a single session
* Semantic retrieval using *FAISS vector search*
* Retrieval-Augmented Generation (RAG) for grounded answers
* Source-aware citations (e.g., "from slide 4" or "at 3:22 in the video")
* Interactive FastAPI Swagger documentation

### 🎓 AI Course Planner

* Multi-turn conversational interface
* Generates:

  * Module breakdown
  * Learning objectives
  * Lesson topics
  * Recommended resources
  * End-of-module assessments
* Supports iterative refinement (e.g., "make Module 2 simpler")
* Live course plan preview
* Export final plan as structured JSON

---

## Tech Stack

### Backend

* Python
* FastAPI
* FAISS
* Google Gemini API
* PyPDF2
* python-pptx
* BeautifulSoup
* youtube-transcript-api

### Frontend

* React
* Vite
* Axios
* React Router

---

## RAG Pipeline


Source
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
FAISS Vector Index
   ↓
Semantic Retrieval
   ↓
Gemini LLM
   ↓
Grounded Response with Citations


---

## Project Structure


multi-source-ai-learning-assistant/

├── backend/
│   ├── routes/
│   ├── services/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md


---

## Installation

### Clone the repository

bash
git clone <repository-url>
cd multi-source-ai-learning-assistant


### Backend

bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt


Create a .env file:

env
GEMINI_API_KEY=your_api_key_here


Run the backend:

bash
uvicorn main:app --reload


Backend: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

---

### Frontend

bash
cd frontend

npm install

npm run dev


Frontend: http://localhost:5173

---

## API Endpoints

| Endpoint            | Description                          |
| ------------------- | ------------------------------------ |
| POST /upload      | Upload and index a PDF               |
| POST /pptx        | Upload and index a PPTX presentation |
| POST /webpage     | Index webpage content                |
| POST /youtube     | Index YouTube transcript             |
| POST /chat        | Query indexed content                |
| POST /course/chat | Create and refine course plans       |

---

## Example Prompts

### Learning Assistant

* Summarize the uploaded PDF.
* What are the key points from slide 5?
* Compare information from the PDF and webpage.
* What does the speaker explain at 2:30 in the video?

### Course Planner

* Create a 6-week Python course for beginners.
* Simplify Module 3.
* Add a capstone project at the end.
* Include free learning resources.

---

## Known Limitations

* *Token-by-token streaming responses are not implemented.* Responses are returned after complete generation.
* *Long conversation memory is limited* and may lose context after several turns.
* *Course plans can be refined through chat*, but direct click-to-edit functionality is not currently available.

---

## Demo
* ## Demo
- **Task 1 Demo:** https://www.loom.com/share/c7921050adff43f396cb17b28d40d023
- **Task 2 Demo:** https://www.loom.com/share/6a0cedf0e64b4de5b9f1d87b414fbed6

---

## Author

*Bhavya Srivastava*
