# Logging setup (query logs, errors)

import os
from datetime import datetime
from app.core.config import settings

def log_query(query: str, answer: str):
    os.makedirs(settings.LOG_DIR, exist_ok=True)
    log_file = os.path.join(settings.LOG_DIR, f"{datetime.today().date()}.log")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] Q: {query}\nA: {answer}\n\n")
