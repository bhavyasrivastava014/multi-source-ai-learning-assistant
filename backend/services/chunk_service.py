def chunk_text(text, chunk_size=1000, overlap=200):
    paragraphs = text.split("\n")

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk.strip())

            # Keep overlap from the end of the previous chunk
            current_chunk = current_chunk[-overlap:] + "\n" + para + "\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
