from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text
from services.embedding_service import create_embeddings
from services.faiss_service import build_index, retrieve_chunks
from services.llm_service import ask_llm
import numpy as np

text = extract_text_from_pdf("uploads/resume (8).pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = build_index(embeddings)

question = "What projects has Bhavya worked on?"

query_embedding = create_embeddings([question])

context = retrieve_chunks(
    index,
    chunks,
    query_embedding,
    3
)

print("\n===== RETRIEVED CHUNKS =====")
for i, chunk in enumerate(context, 1):
    print(f"\nChunk {i}:")
    print(chunk)
print("============================\n")

answer = ask_llm(
    "\n".join(context),
    question
)

print(answer)
