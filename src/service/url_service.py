from src.dto.url_response import UrlResponse, Redirect
from src.entity.url_mapping import UrlMapping
from src.repository.url_repository import UrlRepository
from src.util.base_62_encoding import generate_short_code
from typing import Optional


class UrlService:

    def __init__(self, repository: UrlRepository):
        self.repository = repository

    def create_short_url(self, long_url: str):

        short_code = generate_short_code()

        url_mapping = UrlMapping(
            short_code=short_code,
            long_url=long_url,
            click_count=0,
        )

        saved = self.repository.save(url_mapping)

        return UrlResponse(
            short_code=f"https://localhost:8000/{saved.short_code}",
        )
    
    
    def get_long_url(self, short_code: str) -> Redirect:
        try:
            url_mapping = self.repository.get_url_mapping_by_short_code(short_code)
        except Exception as e:
            raise Exception(f"Error occurred while fetching URL mapping: {e}")

        return Redirect(long_url=url_mapping.long_url)
    
    def check_existing_url(self, long_url: str) -> Optional[UrlResponse]:
        
        existing_mapping = self.repository.check_long_url_exists(long_url)
        if existing_mapping:
            return UrlResponse(short_code=f"https://localhost:8000/{existing_mapping.short_code}")
        return None
    