import faiss
import numpy as np


def build_index(embeddings):
    embeddings = np.array(embeddings, dtype=np.float32)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    return index


def retrieve_chunks(index, chunks, query_embedding, k=3):
    query_embedding = np.array(query_embedding, dtype=np.float32)

    # Ensure shape is (1, embedding_dim)
    if query_embedding.ndim == 1:
        query_embedding = query_embedding.reshape(1, -1)

    distances, indices = index.search(query_embedding, k)

    print("Distances:", distances)
    print("Indices:", indices)

    results = []

    for idx in indices[0]:
        if 0 <= idx < len(chunks):
            results.append(chunks[idx])

    return results