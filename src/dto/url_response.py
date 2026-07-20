from pydantic import BaseModel


class UrlResponse(BaseModel):
    short_url: str