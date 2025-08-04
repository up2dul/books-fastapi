dev:
	uv run uvicorn app.main:app --reload

format:
	uv run ruff format
	uv run ruff check --fix

db-migrate:
	uv run alembic upgrade head