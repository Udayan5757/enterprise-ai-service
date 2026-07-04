from fastapi import APIRouter

from src.services.ingestion_service import IngestionService

router = APIRouter()

@router.post("/rebuild")
def rebuild():

    IngestionService().ingest()

    return {
        "message": "Knowledge Base Rebuilt Successfully"
    }