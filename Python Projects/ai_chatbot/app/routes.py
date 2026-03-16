from fastapi import APIRouter
from app.chatbot import get_reply

router = APIRouter()

@router.post("/chat")
def chat(message: str):
    reply = get_reply(message)
    return {"reply": reply}