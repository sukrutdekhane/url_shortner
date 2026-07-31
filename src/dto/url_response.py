from pydantic import BaseModel


class UrlResponse(BaseModel):
    short_code: str

class Redirect(BaseModel):
    long_url: str