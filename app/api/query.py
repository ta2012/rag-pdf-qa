from fastapi import APIRouter, HTTPException
from app.models.schemas import QueryRequest, AnswerResponse
from app.rag.pipeline import answer_question
from app.services.vector_store import vector_store

router = APIRouter(prefix="/query", tags=["query"])

@router.post("/", response_model=AnswerResponse)
async def query_document(payload: QueryRequest):
    if not vector_store.has_document(payload.document_id):
        raise HTTPException(status_code=404, detail="Document not found")

    answer, context_chunks = answer_question(
        document_id=payload.document_id,
        question=payload.question,
        top_k=payload.top_k,
    )

    return AnswerResponse(
        answer=answer,
        context_chunks=context_chunks,
    )
