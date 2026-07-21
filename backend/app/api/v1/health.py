from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health_check() -> dict[str, str]:
    """Check whether the application is running."""
    return {
        "status": "healthy",
        "service": "GenAssist AI",
        "version": "1.0.0",
    }