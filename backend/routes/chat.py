from fastapi import APIRouter
from pydantic import BaseModel

from services.embedding_service import create_embeddings
from services.faiss_service import retrieve_chunks
from services.llm_service import ask_llm
from services import rag_store


router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(req: ChatRequest):

    if rag_store.CURRENT_INDEX is None:
        return {
            "answer": "Please upload a document first."
        }

    query_embedding = create_embeddings([req.question])

    context = retrieve_chunks(
        rag_store.CURRENT_INDEX,
        rag_store.CURRENT_CHUNKS,
        query_embedding,
        5
    )

    answer = ask_llm(
        "\n".join(context),
        req.question
    )

    return {
        "answer": answer
    }