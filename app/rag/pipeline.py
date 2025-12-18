from typing import List, Tuple
from pathlib import Path

from app.services.pdf_loader import load_pdf_pages
from app.services.text_preprocess import normalize_pages
from app.services.chunker import chunk_pages
from app.services.embeddings import embed_texts, get_embedding_model
from app.services.vector_store import vector_store

def ingest_pdf(document_id: str, pdf_path: Path) -> Tuple[int, int]:
    pages = load_pdf_pages(pdf_path)
    clean_pages = normalize_pages(pages)
    chunks = chunk_pages(clean_pages)
    embeddings = embed_texts(chunks)

    vector_store.add_document(document_id, embeddings, chunks)
    return len(pages), len(chunks)

def answer_question(document_id: str, question: str, top_k: int = 5) -> Tuple[str, List[str]]:
    model = get_embedding_model()
    q_emb = model.encode([question], normalize_embeddings=True)[0]

    context_chunks = vector_store.similarity_search(
        document_id=document_id,
        query_embedding=q_emb,
        top_k=top_k,
    )

    if not context_chunks:
        answer = "I could not find relevant information in the document for this question."
    else:
        # Simple extractive style: return concatenated top chunks
        answer = (
            "Here are the most relevant parts from the document:\n\n"
            + "\n\n---\n\n".join(context_chunks)
        )

    return answer, context_chunks
