from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from scalar_fastapi import get_scalar_api_reference

from app.routes import books_router
from app.settings import settings

app = FastAPI(
    title=settings.APP_NAME, version=settings.APP_VERSION, docs_url=settings.DOC_URL
)

app.include_router(books_router)


@app.get("/")
def hello() -> dict[str, str]:
    return {
        "message": "Go to /scalar to see the OpenAPI reference",
        "title": app.title,
        "version": app.version,
    }


@app.get("/scalar", include_in_schema=False)
def scalar_html() -> HTMLResponse:
    if not app.openapi_url:
        raise RuntimeError("OpenAPI URL is not set.")
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
