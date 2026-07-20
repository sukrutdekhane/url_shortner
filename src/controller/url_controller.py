from fastapi import APIRouter

from src.core.database import SessionLocal
from src.repository.url_repository import UrlRepository
from src.service.url_service import UrlService

router = APIRouter()

@router.post("/urls/shorten")
def shorten_url(long_url: str):
    db = SessionLocal()

    try:
        repository = UrlRepository(db)
        service = UrlService(repository)

        return service.create_short_url(long_url)

    finally:
        db.close()