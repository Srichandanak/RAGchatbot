# app/api/upload.py
from fastapi import APIRouter, UploadFile, File
import shutil, os
from app.services.rag_pipeline import ingest_document

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Ingest into RAG pipeline
    ingest_document(file_path)

    return {"filename": file.filename, "message": "File uploaded and ingested successfully"}
