from typing import Optional

from sqlalchemy.orm import Session

from src.entity.url_mapping import UrlMapping
from fastapi import HTTPException


class UrlRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, url_mapping: UrlMapping) -> UrlMapping:
        self.db.add(url_mapping)
        self.db.commit()
        self.db.refresh(url_mapping)

        return url_mapping
    

    def get_url_mapping_by_short_code(self, short_code: str) -> UrlMapping:
        try:
            url_mapping = (
                self.db.query(UrlMapping)
                .filter(UrlMapping.short_code == short_code)
                .first()
            )

            if url_mapping is None:
                raise HTTPException(status_code=404, detail="Short URL not found")

            url_mapping.click_count += 1

            self.db.commit()
            self.db.refresh(url_mapping)

            return url_mapping

        except Exception as e:
            print(f"Error occurred while fetching URL mapping: {e}")
            raise
    
    def check_long_url_exists(self, long_url: str) -> Optional[UrlMapping]:
        try:
            url_mapping = (
                self.db.query(UrlMapping)
                .filter(UrlMapping.long_url == long_url)
                .first()
            )
            if url_mapping is None:
                return None
            
            url_mapping.click_count += 1
            
            return url_mapping

        except Exception as e:
            print(f"Error occurred while checking long URL existence: {e}")
            raise