from fastapi import APIRouter, UploadFile, File
import os
import shutil

from services.ppt_service import extract_text_from_ppt
from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text
from services.embedding_service import create_embeddings
from services.faiss_service import build_index
from services import rag_store

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the file based on its type
    if file.filename.lower().endswith(".pdf"):
      text = extract_text_from_pdf(file_path)

    elif file.filename.lower().endswith((".ppt", ".pptx")):
      text = extract_text_from_ppt(file_path)

    else:
      return {
        "message": "Unsupported file type",
        "filename": file.filename,
      }

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    index = build_index(embeddings)

    rag_store.CURRENT_CHUNKS = chunks
    rag_store.CURRENT_INDEX = index

    return {
        "message": "File uploaded and indexed successfully",
        "filename": file.filename, "chunks": len(chunks),
    }
