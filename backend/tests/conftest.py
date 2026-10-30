import os

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

# Force test configuration
os.environ["ENVIRONMENT"] = "test"
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"
os.environ["DATABASE_SYNC_URL"] = "sqlite:///./test.db"
os.environ["REDIS_URL"] = "redis://localhost:6379/15"

from app.core.config import settings
from app.core.database import Base, engine
from app.main import create_app


@pytest_asyncio.fixture(autouse=True)
async def prepare_database():
    settings.ensure_directories()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()
    if os.path.exists("./test.db"):
        try:
            os.remove("./test.db")
        except OSError:
            pass


@pytest_asyncio.fixture
async def async_client():
    app = create_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client
