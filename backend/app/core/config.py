import os

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True
    )

    APP_NAME: str = "AI Vision Trainer"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "temporary-development-secret-key-32-chars-min-change-prod"

    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]

    @field_validator("CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        return []

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://vision_user:vision_password@localhost:5432/ai_vision_trainer"
    DATABASE_SYNC_URL: str = "postgresql://vision_user:vision_password@localhost:5432/ai_vision_trainer"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Storage paths
    STORAGE_ROOT: str = "./storage"
    DATASET_STORAGE_PATH: str = "./storage/datasets"
    MODEL_STORAGE_PATH: str = "./storage/models"
    ARTIFACT_STORAGE_PATH: str = "./storage/artifacts"
    UPLOAD_TEMP_PATH: str = "./storage/temp_uploads"

    # Accelerator
    ACCELERATOR_DEVICE: str = "auto"

    def ensure_directories(self) -> None:
        """Ensure critical storage subdirectories exist."""
        for path in [
            self.STORAGE_ROOT,
            self.DATASET_STORAGE_PATH,
            self.MODEL_STORAGE_PATH,
            self.ARTIFACT_STORAGE_PATH,
            self.UPLOAD_TEMP_PATH,
        ]:
            os.makedirs(path, exist_ok=True)


settings = Settings()
