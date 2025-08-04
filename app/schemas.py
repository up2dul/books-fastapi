from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    """Base schema for book data."""

    title: str
    author: str
    year: int
    genre: Optional[str] = None


class BookRead(BookBase):
    """Schema for reading a book."""

    id: int


class BookCreate(BookBase):
    """Schema for creating a new book."""

    pass


class BookUpdate(BaseModel):
    """Schema for updating a book."""

    id: int
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
