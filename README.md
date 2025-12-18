#  PDF RAG QA

Retrieval-Augmented Generation backend for question-answering over your own PDFs using **FastAPI**, **Sentence Transformers (all‑MiniLM‑L6‑v2)**, and **ChromaDB**. No OpenAI key required. 

---

##  Stack

- FastAPI + Uvicorn [web:114]  
- SentenceTransformers `all-MiniLM-L6-v2` (384‑d embeddings) 
- ChromaDB vector store (persistent)   
- pypdf for PDF text extraction  
- Python 3.12

---

##  Structure

## Structure

- `app/` – API, config, models, services, RAG pipeline, main app
- `data/uploads/` – uploaded PDFs (ignored)
- `data/chroma/` – ChromaDB index (ignored)
- `tests/` – unit tests
- `requirements.txt`
- `README.md`

##  RAG Flow

1. **Ingest (`POST /ingest`)**  
   - Upload PDF → extract text (pypdf).  
   - Normalize text, split into 800‑char chunks with 200 overlap.  
   - Encode with `all-MiniLM-L6-v2` → 384‑d embeddings. 
   - Store chunks + embeddings in Chroma.

2. **Query (`POST /query`)**  
   - Embed question with same model.  
   - Chroma top‑k similarity search returns relevant chunks. 
   - Current version returns an extractive answer by concatenating those chunks (LLM‑agnostic).
  
## 🛠 Ideas

- Plug an LLM into `app/rag/pipeline.py` for generated answers.  
- Add a small frontend (React/Next/Streamlit) on top of this API.


