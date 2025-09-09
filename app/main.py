#FAstAPI entrypoint (starts the app)

from fastapi import FastAPI
from app.api import chat, stt, tts

app = FastAPI(title="College Chatbot", version="1.0")

# Register routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(stt.router, prefix="/stt", tags=["Speech-to-Text"])
app.include_router(tts.router, prefix="/tts", tags=["Text-to-Speech"])

@app.get("/")
def root():
    return {"message": "College Chatbot Backend is running 🚀"}
