#FAstAPI entrypoint (starts the app)

from fastapi import FastAPI
from app.api import chat, stt, tts, upload

app = FastAPI(title="College Chatbot", version="1.0")
# app/main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(stt.router, prefix="/stt", tags=["Speech-to-Text"])
app.include_router(tts.router, prefix="/tts", tags=["Text-to-Speech"])
app.include_router(upload.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "College Chatbot Backend is running 🚀"}
