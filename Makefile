SHELL := /bin/bash

dev:
	uv run uvicorn app.main:app --reload

mcp:
	uv run books_mcp.py

format:
	uv run ruff format
	uv run ruff check --fix

db-migrate:
	uv run alembic upgrade head