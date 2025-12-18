from typing import List
from pathlib import Path
import chromadb
from app.core.config import settings

class ChromaVectorStore:
    def __init__(self, persist_dir: Path):
        persist_dir.mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=str(persist_dir))
        self.collection = self.client.get_or_create_collection(
            name="pdf_chunks",
        )

    def add_document(self, document_id: str, embeddings, chunks: List[str]):
        ids = [f"{document_id}_{i}" for i in range(len(chunks))]
        metadatas = [{"document_id": document_id} for _ in chunks]
        self.collection.add(
            ids=ids,
            embeddings=embeddings.tolist(),
            documents=chunks,
            metadatas=metadatas,
        )

    def has_document(self, document_id: str) -> bool:
        res = self.collection.get(
            where={"document_id": document_id},
            limit=1,
        )
        return len(res.get("ids", [])) > 0

    def similarity_search(
        self,
        document_id: str,
        query_embedding,
        top_k: int = 5,
    ) -> List[str]:
        res = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            where={"document_id": document_id},
            n_results=top_k,
        )
        return res.get("documents", [[]])[0]

vector_store = ChromaVectorStore(settings.VECTOR_DB_DIR)
