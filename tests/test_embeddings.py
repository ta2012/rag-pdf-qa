from app.services.embeddings import embed_texts, get_embedding_model

def test_embedding_model_loads():
    model = get_embedding_model()
    # Model name check optional, but helpful
    assert model is not None

def test_embed_texts_shape():
    texts = ["hello world", "this is a test"]
    embeddings = embed_texts(texts)

    # 2 texts → 2 vectors
    assert embeddings.shape[0] == 2
    # all-MiniLM-L6-v2 = 384-dim
    assert embeddings.shape[1] == 384
