import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root_endpoint(async_client: AsyncClient):
    response = await async_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "AI Vision Trainer"
    assert data["version"] == "1.0.0"
    assert "documentation" in data


@pytest.mark.asyncio
async def test_simple_health_endpoint(async_client: AsyncClient):
    response = await async_client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] in ["healthy", "degraded", "unhealthy"]
    assert data["app_name"] == "AI Vision Trainer"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_detailed_health_endpoint(async_client: AsyncClient):
    response = await async_client.get("/api/v1/health/detailed")
    assert response.status_code == 200
    data = response.json()

    # Core response assertions
    assert data["app_name"] == "AI Vision Trainer"
    assert "uptime_seconds" in data
    assert data["uptime_seconds"] >= 0

    # Database assertions
    assert "database" in data
    assert data["database"]["status"] in ["connected", "disconnected"]
    assert data["database"]["engine"] in ["sqlite", "postgresql"]

    # Redis assertions
    assert "redis" in data
    assert data["redis"]["status"] in ["connected", "disconnected", "unresponsive"]

    # Hardware assertions
    assert "hardware" in data
    hw = data["hardware"]
    assert "cpu_percent" in hw
    assert "memory_percent" in hw
    assert "disk_free_gb" in hw
    assert "accelerator" in hw
    assert isinstance(hw["accelerator_available"], bool)
