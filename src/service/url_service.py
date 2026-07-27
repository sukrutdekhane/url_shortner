from src.dto.url_response import UrlResponse
from src.entity.url_mapping import UrlMapping
from src.repository.url_repository import UrlRepository
from src.util.base_62_encoding import generate_short_code


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
            long_url=f"{saved.short_code}"
        )
    
    def get_long_url(self, short_code: str) -> UrlResponse:
        try:
            url_mapping = self.repository.get_url_mapping_by_short_code(short_code)
        except Exception as e:
            raise Exception(f"Error occurred while fetching URL mapping: {e}")

        return UrlResponse(long_url=url_mapping.long_url)