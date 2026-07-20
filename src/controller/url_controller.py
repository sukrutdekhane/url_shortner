from fastapi import APIRouter

from src.core.database import SessionLocal
from src.dto.url_request import UrlRequest
from src.repository.url_repository import UrlRepository
from src.service.url_service import UrlService

router = APIRouter()


@router.post("/urls/shorten")
def shorten_url(request: UrlRequest):

    db = SessionLocal()

    try:
        repository = UrlRepository(db)
        service = UrlService(repository)

        return service.create_short_url(request.long_url)

    finally:
        db.close()