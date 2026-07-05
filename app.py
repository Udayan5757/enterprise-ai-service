from fastapi import FastAPI
from src.api.routes import router
from src.api.upload_routes import router as upload_router

app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    version="1.0.0"
)

app.include_router(router)
app.include_router(upload_router)