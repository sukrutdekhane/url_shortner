from src.dto.url_response import UrlResponse
from src.entity.url_mapping import UrlMapping
from src.repository.url_repository import UrlRepository
from src.util.base_62_encoding import generate_short_code


class UrlService:

    def __init__(self, repository: UrlRepository):
        self.repository = repository

    def create_short_url(self, long_url: str):
        if self.repository.check_long_url_exists(long_url):
            raise ValueError("Long URL already exists in the database.")
        
        short_code = generate_short_code()

        while True:            
            if self.repository.check_short_code_exists(short_code):
                short_code = generate_short_code()
            else:
                break

        url_mapping = UrlMapping(
            short_code=short_code,
            long_url=long_url,
            click_count=0,
        )

        self.repository.save(url_mapping)