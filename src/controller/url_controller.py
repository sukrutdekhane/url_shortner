from fastapi import APIRouter

from src.core.database import SessionLocal
from src.dto.url_request import UrlRequest
from src.repository.url_repository import UrlRepository
from src.service.url_service import UrlService
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/urls/shorten")
def shorten_url(request: UrlRequest):

    db = SessionLocal()

    try:
        # Add a code to check whether the URL already exists in the database and return the existing short code if it does.
        repository = UrlRepository(db)
        service = UrlService(repository)
        
        if not request.long_url.startswith(("http://", "https://")):
            request.long_url = "https://" + request.long_url
            
        existing_url = service.check_existing_url(request.long_url)
        
        if existing_url:
            return existing_url
        
        return service.create_short_url(request.long_url)

    finally:
        db.close()

@router.get("/{short_code}")
def redirect_to_long_url(short_code: str):
    db = SessionLocal()

    try:
        repository = UrlRepository(db)
        service = UrlService(repository)

        url_mapping = service.get_long_url(short_code)

        return RedirectResponse(
            url=url_mapping.long_url,
            status_code=302
        )

    finally:
        db.close()