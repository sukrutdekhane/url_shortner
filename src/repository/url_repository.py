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