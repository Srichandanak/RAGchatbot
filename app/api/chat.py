# /chat endpoint (RAG pipeline)

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_pipeline import qa_chain
from app.services.translation import multilingual_qa
from app.core.logger import log_query

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/")
async def chat_endpoint(req: ChatRequest):
    answer = multilingual_qa(req.query, qa_chain)
    log_query(req.query, answer)
    return {"query": req.query, "answer": answer}
