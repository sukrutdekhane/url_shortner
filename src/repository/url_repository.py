from sqlalchemy.orm import Session

from src.entity.url_mapping import UrlMapping


class UrlRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, url_mapping: UrlMapping) -> UrlMapping:
        self.db.add(url_mapping)
        self.db.commit()
        self.db.refresh(url_mapping)

        return url_mapping
    
    def check_long_url_exists(self, long_url: str) -> bool:
        return self.db.query(UrlMapping).filter(UrlMapping.long_url == long_url).first() is not None