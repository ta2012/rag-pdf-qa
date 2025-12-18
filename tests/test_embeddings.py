from app.services.embeddings import embed_texts, get_embedding_model

def test_embedding_model_loads():
    model = get_embedding_model()
    
    assert model is not None

def test_embed_texts_shape():
    texts = ["hello world", "this is a test"]
    embeddings = embed_texts(texts)

    
    assert embeddings.shape[0] == 2
    
    assert embeddings.shape[1] == 384


