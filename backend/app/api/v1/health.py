from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health_check(
    db: AsyncSession = Depends(get_db),
) -> dict[str, str]:
    """Check application and database health."""

    await db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "service": "GenAssist AI",
        "database": "connected",
    }