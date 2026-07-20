from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.database import Base, engine

# Import all entities
from src.entity.url_mapping import UrlMapping


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting application...")

    # Create tables
    Base.metadata.create_all(bind=engine)

    yield

    print("Stopping application...")


app = FastAPI(lifespan=lifespan)