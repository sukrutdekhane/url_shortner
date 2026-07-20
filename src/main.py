from fastapi import FastAPI

from src.controller.url_controller import router as url_router

app = FastAPI(
    title="URL Shortener",
    version="1.0.0"
)

app.include_router(url_router)