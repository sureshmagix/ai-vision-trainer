from pathlib import Path

import pytest
from app.core.security import sanitize_path
from fastapi import HTTPException
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_security_headers(async_client: AsyncClient):
    response = await async_client.get("/api/v1/health")
    assert response.status_code == 200
    headers = response.headers

    assert headers.get("X-Content-Type-Options") == "nosniff"
    assert headers.get("X-Frame-Options") == "DENY"
    assert headers.get("X-XSS-Protection") == "1; mode=block"
    assert headers.get("Referrer-Policy") == "strict-origin-when-cross-origin"


@pytest.mark.asyncio
async def test_cors_options_preflight(async_client: AsyncClient):
    headers = {
        "Origin": "http://localhost:5173",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "authorization,content-type",
    }
    response = await async_client.options("/api/v1/health", headers=headers)
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "http://localhost:5173"


@pytest.mark.asyncio
async def test_404_not_found_handling(async_client: AsyncClient):
    response = await async_client.get("/api/v1/non-existent-endpoint")
    assert response.status_code == 404


def test_path_traversal_sanitization(tmp_path: Path):
    base_storage = tmp_path / "storage"
    base_storage.mkdir()

    # Valid child path
    valid = sanitize_path("dataset_1/images", base_dir=str(base_storage))
    assert str(valid).startswith(str(base_storage))

    # Path traversal attack attempts
    with pytest.raises(HTTPException) as exc_info:
        sanitize_path("../../../etc/passwd", base_dir=str(base_storage))
    assert exc_info.value.status_code == 400
    assert "Illegal path traversal" in exc_info.value.detail

    with pytest.raises(HTTPException):
        sanitize_path("foo/../../sensitive_system_file", base_dir=str(base_storage))
