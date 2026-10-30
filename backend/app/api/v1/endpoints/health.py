from app.schemas.health import DetailedHealthResponse, SimpleHealthResponse
from app.services.health_service import get_detailed_health, get_simple_health
from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/health",
    response_model=SimpleHealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Simple System Health Check",
    description="Returns high-level health status of the application.",
)
async def check_health() -> SimpleHealthResponse:
    return await get_simple_health()


@router.get(
    "/health/detailed",
    response_model=DetailedHealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Detailed Health and Diagnostic Metrics",
    description="Returns connectivity status for Database and Redis, alongside live CPU, RAM, and GPU accelerator telemetry.",
)
async def check_detailed_health() -> DetailedHealthResponse:
    return await get_detailed_health()
