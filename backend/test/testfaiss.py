from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text
from services.embedding_service import create_embeddings
from services.faiss_service import build_index

text = extract_text_from_pdf("uploads/resume (8).pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = build_index(embeddings)

print(index.ntotal)
