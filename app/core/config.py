# Environment variables (API keys, paths, etc.)

# Environment variables (API keys, paths, etc.)

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

    # Only static PDFs you want preloaded at startup
    PDF_PATHS: list[str] = [
        "data/pdfs/RMDEC UG Regulation 2022.pdf",
        "data/pdfs/BATCH 2027 R2022 B.Tech AIML FINAL.pdf"
    ]

    # Upload directory (for runtime ingestion)
    UPLOAD_DIR: str = "uploads"

    VECTORDB_PATH: str = "data/vectordb"
    LOG_DIR: str = "data/logs"

settings = Settings()
