import numpy as np
from pathlib import Path
from app.services.vector_store import ChromaVectorStore

def test_add_and_has_document(tmp_path: Path):
    store = ChromaVectorStore(tmp_path / "chroma_test")

    document_id = "doc-1"
    chunks = ["first chunk text", "second chunk text"]
    # Fake embeddings: 2 vectors of 384-dim
    embeddings = np.random.rand(2, 384)

    store.add_document(document_id, embeddings, chunks)

    assert store.has_document(document_id) is True

def test_similarity_search(tmp_path: Path):
    store = ChromaVectorStore(tmp_path / "chroma_test2")

    document_id = "doc-2"
    chunks = ["apple banana", "car bus train"]
    embeddings = np.random.rand(2, 384)

    store.add_document(document_id, embeddings, chunks)

    query_embedding = embeddings[0]  # ideally should match first chunk
    results = store.similarity_search(
        document_id=document_id,
        query_embedding=query_embedding,
        top_k=1,
    )

    assert len(results) == 1
    assert isinstance(results[0], str)
