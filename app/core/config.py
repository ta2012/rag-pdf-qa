
from pathlib import Path
from pydantic_settings import BaseSettings  


class Settings(BaseSettings):
    PROJECT_NAME: str = "PDF RAG QA"

    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 200

    DATA_DIR: Path = Path("data")
    UPLOAD_DIR: Path = DATA_DIR / "uploads"
    VECTOR_DB_DIR: Path = DATA_DIR / "chroma"

    class Config:
        env_file = ".env"

settings = Settings()
