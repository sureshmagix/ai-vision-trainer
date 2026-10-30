import time
from typing import Any

import redis.asyncio as aioredis
from app.core.config import settings
from app.core.logging import logger

_redis_client: aioredis.Redis | None = None


def get_redis() -> aioredis.Redis:
    global _redis_client
    if _redis_client is None:
        _redis_client = aioredis.from_url(
            settings.REDIS_URL,
            decode_responses=True,
            socket_timeout=2.0,
            socket_connect_timeout=2.0,
        )
    return _redis_client


async def close_redis() -> None:
    global _redis_client
    if _redis_client is not None:
        await _redis_client.close()
        _redis_client = None


async def check_redis_health() -> dict[str, Any]:
    """Ping Redis broker and measure response latency."""
    client = get_redis()
    start_time = time.perf_counter()
    try:
        pong = await client.ping()
        latency_ms = round((time.perf_counter() - start_time) * 1000, 2)
        if pong:
            return {
                "status": "connected",
                "latency_ms": latency_ms,
            }
        return {
            "status": "unresponsive",
            "latency_ms": latency_ms,
        }
    except Exception as exc:  # noqa: BLE001
        logger.warning(f"Redis health check failed: {exc}")
        return {
            "status": "disconnected",
            "latency_ms": None,
            "error": str(exc),
        }
