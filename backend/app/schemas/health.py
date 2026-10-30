from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class DatabaseHealth(BaseModel):
    status: str = Field(..., description="Status of the database connection")
    latency_ms: float | None = Field(None, description="Query execution latency in milliseconds")
    engine: str = Field(..., description="Database engine type (e.g. postgresql, sqlite)")
    error: str | None = Field(None, description="Error message if disconnected")


class RedisHealth(BaseModel):
    status: str = Field(..., description="Status of the Redis connection")
    latency_ms: float | None = Field(None, description="Ping latency in milliseconds")
    error: str | None = Field(None, description="Error message if disconnected")


class HardwareHealth(BaseModel):
    cpu_percent: float = Field(..., description="Current system CPU utilization percentage")
    memory_percent: float = Field(..., description="System RAM utilization percentage")
    memory_used_gb: float = Field(..., description="RAM used in Gigabytes")
    memory_total_gb: float = Field(..., description="Total system RAM in Gigabytes")
    disk_free_gb: float = Field(..., description="Free storage space in Gigabytes")
    accelerator: str = Field(..., description="Available hardware acceleration device (cuda, mps, or cpu)")
    accelerator_available: bool = Field(..., description="Whether a GPU accelerator is detected")


class SimpleHealthResponse(BaseModel):
    status: Literal["healthy", "degraded", "unhealthy"] = Field(..., description="Overall platform operational status")
    app_name: str
    version: str
    environment: str
    timestamp: datetime


class DetailedHealthResponse(SimpleHealthResponse):
    uptime_seconds: float
    database: DatabaseHealth
    redis: RedisHealth
    hardware: HardwareHealth
