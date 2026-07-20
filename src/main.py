from fastapi import FastAPI

from src.controller.url_controller import router
from src.core.database import Base, engine

# Import entity so SQLAlchemy registers it
from src.entity.url_mapping import UrlMapping

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API"
)

app.include_router(router)