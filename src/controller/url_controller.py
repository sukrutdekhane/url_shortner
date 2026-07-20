from fastapi import APIRouter

from src.service.url_service import UrlService

router = APIRouter()

@router.post("urls/shorten")
def shorten_url(service: UrlService, long_url: str):
    return service.create_short_url(long_url)