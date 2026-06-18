from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.youtube_service import extract_transcript
from services.embedding_service import create_embeddings
from services.chunk_service import chunk_text
from services.faiss_service import build_index
from services import rag_store

router = APIRouter()


class YoutubeRequest(BaseModel):
    url: str


@router.post("/youtube")
def upload_youtube(request: YoutubeRequest):
    try:
        text = extract_transcript(request.url)

        chunks = chunk_text(text)
        embeddings = create_embeddings(chunks)
        index = build_index(embeddings)

        rag_store.CURRENT_CHUNKS = chunks
        rag_store.CURRENT_INDEX = index

        return {
            "message": "YouTube transcript indexed successfully",
            "chunks": len(chunks),
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))