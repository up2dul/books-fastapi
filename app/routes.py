from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)

from app.database import Book, get_db_session
from app.schemas import BookCreate, BookRead, BookUpdate

books_router = APIRouter(prefix="/books", tags=["Books"])


# GET /books - DATA 200
@books_router.get("/", response_model=list[BookRead], status_code=HTTP_200_OK)
def get_books(db: Session = Depends(get_db_session)):
    """Retrieve all books."""
    books = db.exec(select(Book)).all()
    return books


# GET /books/{book_id} - DATA 200
@books_router.get("/{book_id}", response_model=BookRead, status_code=HTTP_200_OK)
def get_book(book_id: int, db: Session = Depends(get_db_session)):
    """Retrieve a book by its ID."""
    db_book = db.get(Book, book_id)
    if not db_book:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book


# PUT /books/{book_id} - DATA 200
@books_router.put("/{book_id}", response_model=BookRead, status_code=HTTP_200_OK)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db_session)):
    """Update a book by its ID."""
    db_book = db.get(Book, book_id)
    if not db_book:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Book not found")

    updated_book = book.model_dump(exclude_unset=True)
    for key, value in updated_book.items():
        setattr(db_book, key, value)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# POST /books - DATA 201
@books_router.post("/", response_model=BookCreate, status_code=HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db_session)):
    """Create a new book."""
    new_book = Book(
        title=book.title, author=book.author, year=book.year, genre=book.genre
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


# DELETE /books/{book_id} - 204
@books_router.delete("/{book_id}", status_code=HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db_session)):
    """Delete a book by its ID."""
    db_book = db.get(Book, book_id)
    if not db_book:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Book not found")

    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted"}
