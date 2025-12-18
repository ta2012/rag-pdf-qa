from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
from pathlib import Path

from app.core.config import settings
from app.models.schemas import IngestResponse
from app.rag.pipeline import ingest_pdf

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/", response_model=IngestResponse)
async def ingest_document(file: UploadFile = File(...)):
    document_id = str(uuid4())

    settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path: Path = settings.UPLOAD_DIR / f"{document_id}.pdf"

    contents = await file.read()
    with open(pdf_path, "wb") as f:
        f.write(contents)

    num_pages, num_chunks = ingest_pdf(document_id, pdf_path)

    return IngestResponse(
        document_id=document_id,
        num_pages=num_pages,
        num_chunks=num_chunks,
    )
