# Wrapper for TTS

import pyttsx3
import os
from datetime import datetime

def text_to_speech(text: str) -> str:
    engine = pyttsx3.init()
    file_path = f"data/logs/tts_{datetime.now().timestamp()}.mp3"
    engine.save_to_file(text, file_path)
    engine.runAndWait()
    return file_path
