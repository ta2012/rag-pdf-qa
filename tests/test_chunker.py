from app.services.chunker import chunk_text

def test_chunk_text_basic():
    text = "a" * 1000
    chunks = chunk_text(text, chunk_size=800, overlap=200)
    assert len(chunks) == 2
    assert len(chunks[0]) == 800
