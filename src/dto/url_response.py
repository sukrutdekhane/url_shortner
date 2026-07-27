from pydantic import BaseModel


class UrlResponse(BaseModel):
    long_url: str