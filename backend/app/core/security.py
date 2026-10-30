from pathlib import Path

from app.core.config import settings
from fastapi import HTTPException, status


def sanitize_path(target_path: str, base_dir: str = settings.STORAGE_ROOT) -> Path:
    """
    Ensure target_path resolves strictly within base_dir to prevent directory traversal.
    Raises HTTPException(400) on path traversal attempts.
    """
    base = Path(base_dir).resolve()
    resolved = (base / target_path).resolve()
    if not str(resolved).startswith(str(base)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Illegal path traversal attempted."
        )
    return resolved
