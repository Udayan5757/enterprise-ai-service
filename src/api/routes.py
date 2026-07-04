from fastapi import APIRouter

from src.models.request import ChatRequest
from src.models.response import ChatResponse
from src.services.chat_service import ChatService

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    chat_service = ChatService()

    result = chat_service.ask(request.question)

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )


@router.get("/health")
def health():

    return {
        "status": "UP"
    }