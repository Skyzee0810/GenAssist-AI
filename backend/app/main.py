from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Production-ready AI-powered knowledge assistant "
        "using Retrieval-Augmented Generation."
    ),
)


app.include_router(
    health_router,
    prefix=settings.api_v1_prefix,
)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """Return basic API information."""
    return {
        "message": "Welcome to GenAssist AI",
        "version": settings.app_version
    }