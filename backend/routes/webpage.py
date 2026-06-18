from fastapi import APIRouter
from pydantic import BaseModel

from services.webpage_service import extract_text_from_url
from services.chunk_service import chunk_text
from services.embedding_service import create_embeddings
from services.faiss_service import build_index
from services import rag_store

router = APIRouter()


class WebpageRequest(BaseModel):
    url: str


@router.post("/webpage")
def process_webpage(request: WebpageRequest):
    text = extract_text_from_url(request.url)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    index = build_index(embeddings)

    rag_store.CURRENT_CHUNKS = chunks
    rag_store.CURRENT_INDEX = index

    return {
        "message": "Webpage indexed successfully",
        "chunks": len(chunks),
    }