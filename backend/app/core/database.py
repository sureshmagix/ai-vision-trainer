import time
from collections.abc import AsyncGenerator
from typing import Any

from app.core.config import settings
from app.core.logging import logger
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

# SQLAlchemy Declarative Base
Base = declarative_base()

# SQLite vs Postgres engine arguments
is_sqlite = settings.DATABASE_URL.startswith("sqlite")
engine_kwargs: dict[str, Any] = {
    "echo": False,
    "future": True,
}

if not is_sqlite:
    engine_kwargs.update({
        "pool_size": settings.DB_POOL_SIZE,
        "max_overflow": settings.DB_MAX_OVERFLOW,
        "pool_pre_ping": True,
    })

engine = create_async_engine(settings.DATABASE_URL, **engine_kwargs)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for providing database sessions per request."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def check_database_health() -> dict[str, Any]:
    """Ping database and measure query latency."""
    engine_type = "sqlite" if is_sqlite else "postgresql"
    start_time = time.perf_counter()
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
            latency_ms = round((time.perf_counter() - start_time) * 1000, 2)
            return {
                "status": "connected",
                "latency_ms": latency_ms,
                "engine": engine_type,
            }
    except Exception as exc:  # noqa: BLE001
        logger.warning(f"Database health check failed: {exc}")
        return {
            "status": "disconnected",
            "latency_ms": None,
            "engine": engine_type,
            "error": str(exc),
        }
