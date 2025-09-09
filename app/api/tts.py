# /tts endpoint (text-to-speech)

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.text_to_speech import text_to_speech

router = APIRouter()

class TTSRequest(BaseModel):
    text: str

@router.post("/")
async def tts_endpoint(req: TTSRequest):
    audio_path = text_to_speech(req.text)
    return {"audio_file": audio_path}
