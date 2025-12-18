from fastapi import FastAPI
from app.core.logging_config import setup_logging
from app.api import ingest, query

setup_logging()

app = FastAPI(title="PDF RAG QA (No LLM)")

app.include_router(ingest.router)
app.include_router(query.router)

@app.get("/")
async def root():
    return {"service": "PDF RAG QA", "status": "running"}
