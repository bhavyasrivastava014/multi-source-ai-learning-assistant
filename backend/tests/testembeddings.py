from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text
from services.embedding_service import create_embeddings

text = extract_text_from_pdf("uploads/resume (8).pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print(embeddings.shape)
