from app.api.v1.endpoints import health
from fastapi import APIRouter

api_v1_router = APIRouter()
api_v1_router.include_router(health.router, tags=["Health & Diagnostics"])
