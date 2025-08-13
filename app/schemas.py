from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    """Base schema for book data."""

    title: str
    author: str
    year: int
    genre: str = "Unknown"


class BookRead(BookBase):
    """Schema for reading a book."""

    id: int


class BookCreate(BookBase):
    """Schema for creating a new book."""

    id: int


class BookUpdate(BaseModel):
    """Schema for updating a book."""

    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
