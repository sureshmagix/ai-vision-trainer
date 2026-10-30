import shutil
import time
from datetime import UTC, datetime

import psutil

from app.core.config import settings
from app.core.database import check_database_health
from app.core.redis import check_redis_health
from app.schemas.health import (
    DatabaseHealth,
    DetailedHealthResponse,
    HardwareHealth,
    RedisHealth,
    SimpleHealthResponse,
)

SERVER_START_TIME = time.time()


def get_hardware_telemetry() -> HardwareHealth:
    """Collect real system hardware metrics via psutil and accelerator status."""
    cpu_pct = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory()

    # Disk usage for storage root
    try:
        disk_usage = shutil.disk_usage(settings.STORAGE_ROOT)
        disk_free_gb = round(disk_usage.free / (1024 ** 3), 2)
    except OSError:
        disk_free_gb = 0.0

    accelerator = "cpu"
    accelerator_available = False

    try:
        import torch
        if torch.cuda.is_available():
            accelerator = f"cuda:{torch.cuda.get_device_name(0)}"
            accelerator_available = True
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            accelerator = "mps (Apple Silicon)"
            accelerator_available = True
    except ImportError:
        pass

    return HardwareHealth(
        cpu_percent=round(cpu_pct, 1),
        memory_percent=round(mem.percent, 1),
        memory_used_gb=round(mem.used / (1024 ** 3), 2),
        memory_total_gb=round(mem.total / (1024 ** 3), 2),
        disk_free_gb=disk_free_gb,
        accelerator=accelerator,
        accelerator_available=accelerator_available,
    )


async def get_simple_health() -> SimpleHealthResponse:
    db_health = await check_database_health()
    status_str = "healthy" if db_health["status"] == "connected" else "unhealthy"

    return SimpleHealthResponse(
        status=status_str,
        app_name=settings.APP_NAME,
        version=settings.APP_VERSION,
        environment=settings.ENVIRONMENT,
        timestamp=datetime.now(UTC),
    )


async def get_detailed_health() -> DetailedHealthResponse:
    db_data = await check_database_health()
    redis_data = await check_redis_health()
    hw_data = get_hardware_telemetry()

    db_health = DatabaseHealth(**db_data)
    redis_health = RedisHealth(**redis_data)

    if db_health.status == "connected" and redis_health.status == "connected":
        overall_status = "healthy"
    elif db_health.status == "connected":
        overall_status = "degraded"
    else:
        overall_status = "unhealthy"

    uptime = round(time.time() - SERVER_START_TIME, 2)

    return DetailedHealthResponse(
        status=overall_status,
        app_name=settings.APP_NAME,
        version=settings.APP_VERSION,
        environment=settings.ENVIRONMENT,
        timestamp=datetime.now(UTC),
        uptime_seconds=uptime,
        database=db_health,
        redis=redis_health,
        hardware=hw_data,
    )
