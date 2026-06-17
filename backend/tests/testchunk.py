from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text

text = extract_text_from_pdf("uploads/resume (8).pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)
    