# Multi-Source AI Learning Assistant

## Overview

The Multi-Source AI Learning Assistant is a FastAPI-based application that allows users to upload and query information from multiple sources using Retrieval-Augmented Generation (RAG). It supports documents, webpages, and YouTube videos, enabling users to ask natural language questions about the indexed content.

## Features

* Upload and chat with PDF documents
* Extract and chat with webpage content
* Extract and chat with YouTube video transcripts
* Semantic search using vector embeddings
* Retrieval-Augmented Generation (RAG) for contextual responses
* RESTful API with interactive Swagger documentation

## Tech Stack

* Python
* FastAPI
* FAISS
* Google Gemini API
* youtube-transcript-api
* BeautifulSoup
* PyPDF2
* Uvicorn

## Project Structure

```
backend/
│── routes/
│   ├── upload.py
│   ├── webpage.py
│   ├── youtube.py
│   └── chat.py
│
│── services/
│   ├── embedding_service.py
│   ├── youtube_service.py
│   ├── webpage_service.py
│   ├── pdf_service.py
│   └── rag_store.py
│
│── main.py
│── requirements.txt
│── .env
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a `.env` file

```
GEMINI_API_KEY=your_api_key_here
```

## Run the Project

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to access the Swagger UI.

## API Endpoints

### Upload a Document

**POST** `/upload`

Uploads and indexes a supported document for question answering.

---

### Index a Webpage

**POST** `/webpage`

Extracts webpage content and stores it for semantic retrieval.

---

### Index a YouTube Video

**POST** `/youtube`

Extracts the transcript of a YouTube video and indexes it for querying.

Example request:

```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

---

### Chat with Indexed Content

**POST** `/chat`

Ask questions about the currently indexed content.

Example request:

```json
{
  "question": "Summarize the uploaded content."
}
```

## Author

Bhavya Srivastava
