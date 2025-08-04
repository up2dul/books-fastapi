import os
from typing import Optional

from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine

load_dotenv(override=True)
engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///./dev-books.db"))


def get_db_session():
    """Get a database session."""
    with Session(engine) as session:
        yield session


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field()
    author: str = Field()
    year: int = Field()
    genre: Optional[str] = Field(default="Unknown")
