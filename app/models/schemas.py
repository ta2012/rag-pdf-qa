from pydantic import BaseModel
from typing import List

class IngestResponse(BaseModel):
    document_id: str
    num_pages: int
    num_chunks: int

class QueryRequest(BaseModel):
    document_id: str
    question: str
    top_k: int = 5

class AnswerResponse(BaseModel):
    answer: str
    context_chunks: List[str]
