# 📚 Books RESTful API

A simple and elegant RESTful API for managing a books collection, built with **FastAPI**, **SQLite**, and **Docker**. This project serves as a learning exercise for building modern Python web APIs with automatic documentation, database migrations, and containerization.

## ✨ Features

- 🚀 **FastAPI** - High-performance, easy-to-use web framework
- 📊 **SQLite** - Lightweight, file-based database
- 🗃️ **SQLModel** - SQL databases in Python, designed for simplicity and type safety
- 📖 **Automatic API Documentation** - Interactive docs with Scalar UI
- 🤖 **MCP Integration** - Model Context Protocol server for AI assistant integration
- 🐳 **Docker** - Containerized deployment
- 🗄️ **Alembic** - Database migration management
- 🎨 **UV** - Fast Python package manager
- 🔧 **Ruff** - Lightning-fast Python linter and formatter

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: SQLite with SQLModel ORM
- **Migration**: Alembic
- **Package Management**: UV
- **Containerization**: Docker
- **Code Quality**: Ruff (linting & formatting)

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and API info |
| GET | `/scalar` | Interactive API documentation |
| GET | `/books` | Get all books |
| POST | `/books` | Create a new book |
| GET | `/books/{id}` | Get a book by ID |
| PUT | `/books/{id}` | Update a book |
| DELETE | `/books/{id}` | Delete a book |

## 🏗️ Project Structure

```
books-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── database.py      # Database configuration
│   ├── routes.py        # API route definitions
│   ├── schemas.py       # Pydantic models for request/response
│   └── settings.py      # Application settings
├── migrations/          # Alembic database migrations
│   ├── env.py
│   └── versions/
├── alembic.ini         # Alembic configuration
├── books_mcp.py       # Model Context Protocol server
├── pyproject.toml      # Project dependencies and configuration
├── uv.lock            # Lock file for dependencies
├── Dockerfile         # Docker container configuration
├── Makefile          # Development commands
└── README.md         # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [UV](https://docs.astral.sh/uv/) package manager
- Docker (optional, for containerized deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/up2dul/books-fastapi.git

   # or if using ssh
   git clone git@github.com:up2dul/books-fastapi.git

   # open the project folder
   cd books-fastapi
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run database migrations**
   ```bash
   make db-migrate
   # or
   uv run alembic upgrade head
   ```

4. **Start the development server**
   ```bash
   make dev
   # or
   uv run uvicorn app.main:app --reload
   ```

5. **Visit the API**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/scalar
   - OpenAPI Schema: http://localhost:8000/openapi.json

### 🐳 Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t books-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 books-api
   ```

The API will be available at http://localhost:8000

## 📝 Usage Examples

### Create a Book
```bash
curl -X POST "http://localhost:8000/books" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "The Devotion of Suspect X",
       "author": "Keigo Higashino",
       "year": 2005,
       "genre": "Fiction"
     }'
```

### Get All Books
```bash
curl -X GET "http://localhost:8000/books"
```

### Get a Specific Book
```bash
curl -X GET "http://localhost:8000/books/1"
```

### Update a Book
```bash
curl -X PUT "http://localhost:8000/books/1" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "The Devotion of Suspect X - Updated",
       "year": 2005
     }'
```

### Delete a Book
```bash
curl -X DELETE "http://localhost:8000/books/1"
```

## 🗄️ Database Schema

### Book Model

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | Integer | Auto | Primary key |
| title | String | Yes | Book title |
| author | String | Yes | Author name |
| year | Integer | Yes | Publication year |
| genre | String | No | Book genre |

## 🤖 Model Context Protocol (MCP) Integration

This project includes an MCP server that provides AI assistants with tools to interact with the Books API. The MCP server exposes the following tools:

- `get_books()` - Retrieve all books
- `get_book(book_id)` - Get a specific book by ID
- `create_book(title, author, year, genre)` - Create a new book
- `update_book(book_id, title, author, year, genre)` - Update an existing book
- `delete_book(book_id)` - Delete a book by ID

### Running the MCP Server

1. **Start the FastAPI server first**
   ```bash
   make dev
   ```

2. **In a separate terminal, start the MCP server**
   ```bash
   make mcp
   # or
   uv run books_mcp.py
   ```

The MCP server will run on port 8001 and will be available for AI assistants to connect and interact with your books database through the defined tools.

## 🔧 Development Commands

```bash
# Start development server with auto-reload
make dev

# Start MCP server (requires API server to be running)
make mcp

# Format code and fix linting issues
make format

# Run database migrations
make db-migrate

# Create new migration
uv run alembic revision --autogenerate -m "description"

# Check code quality
uv run ruff check
uv run ruff format --check
```

## 🌟 Learning Outcomes

This project demonstrates:

- **FastAPI Framework**: Building REST APIs with automatic documentation
- **Database Integration**: Using SQLModel for database operations
- **Migration Management**: Handling database schema changes with Alembic
- **Modern Python**: Type hints, Pydantic models, and async/await patterns
- **API Design**: RESTful principles and HTTP status codes
- **MCP Integration**: Creating Model Context Protocol servers for AI assistant integration
- **Containerization**: Docker best practices for Python applications
- **Development Workflow**: Code formatting, linting, and development automation

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)

---
