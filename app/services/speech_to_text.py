# Wrapper for STT

import speech_recognition as sr

def speech_to_text(file) -> str:
    recognizer = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception:
        return "Sorry, I could not transcribe the audio."
