from fastapi import APIRouter, UploadFile, File

from src.services.upload_service import UploadService

router = APIRouter()


@router.post("/upload")
def upload(file: UploadFile = File(...)):

    service = UploadService()

    return service.upload(file)