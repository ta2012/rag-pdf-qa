from typing import List
from app.core.config import settings

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    chunks: List[str] = []
    start = 0
    length = len(text)

    if length == 0:
        return chunks

    while start < length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = start + chunk_size - overlap

    return chunks

def chunk_pages(pages: List[str]) -> List[str]:
    all_chunks: List[str] = []
    for page_text in pages:
        if not page_text.strip():
            continue
        page_chunks = chunk_text(
            page_text,
            chunk_size=settings.CHUNK_SIZE,
            overlap=settings.CHUNK_OVERLAP,
        )
        all_chunks.extend(page_chunks)
    return all_chunks
