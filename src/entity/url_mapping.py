from sqlalchemy import BigInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class UrlMapping(Base):
    __tablename__ = "url_mapping"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    short_code: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
    )

    long_url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    click_count: Mapped[int] = mapped_column(
        BigInteger,
        default=0,
    )