 # /stt endpoint (speech-to-text)

from fastapi import APIRouter, UploadFile, File
from app.services.speech_to_text import speech_to_text

router = APIRouter()

@router.post("/")
async def stt_endpoint(file: UploadFile = File(...)):
    text = speech_to_text(file.file)
    return {"transcription": text}
