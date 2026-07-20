from src.dto.url_response import UrlResponse
from src.entity.url_mapping import UrlMapping
from src.repository.url_repository import UrlRepository


class UrlService:

    def __init__(self, repository: UrlRepository):
        self.repository = repository

    def create_short_url(self, long_url: str):

        # Replace this with your Base62 logic later
        short_code = "AbC123"

        url_mapping = UrlMapping(
            short_code=short_code,
            long_url=long_url,
            click_count=0,
        )

        saved = self.repository.save(url_mapping)

        return UrlResponse(
            short_url=f"http://localhost:8000/{saved.short_code}"
        )