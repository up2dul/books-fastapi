from fastmcp import FastMCP
from requests import delete, get, post, put

mcp = FastMCP("My books RESTful API MCP server", port=8001)

BASE_URL = "http://localhost:8000"


@mcp.tool()
def get_books() -> list[dict]:
    """Get all books."""
    try:
        response = get(f"{BASE_URL}/books")
        return response.json()
    except Exception as e:
        print(e)
        return []


@mcp.tool()
def get_book(book_id: int) -> dict:
    """Get a book by its ID."""
    try:
        response = get(f"{BASE_URL}/books/{book_id}")
        return response.json()
    except Exception as e:
        print(e)
        return {}


@mcp.tool()
def create_book(title: str, author: str, year: int, genre: str = "Unknown") -> dict:
    """Create a new book."""
    try:
        response = post(
            f"{BASE_URL}/books",
            json={
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
            },
        )
        return response.json()
    except Exception as e:
        print(e)
        return {}


@mcp.tool()
def update_book(
    book_id: int, title: str, author: str, year: int, genre: str = "Unknown"
) -> dict:
    """Update a book by its ID."""
    try:
        response = put(
            f"{BASE_URL}/books/{book_id}",
            json={
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
            },
        )
        return response.json()
    except Exception as e:
        print(e)
        return {}


@mcp.tool()
def delete_book(book_id: int) -> dict:
    """Delete a book by its ID."""
    try:
        response = delete(f"{BASE_URL}/books/{book_id}")
        return response.json()
    except Exception as e:
        print(e)
        return {}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
