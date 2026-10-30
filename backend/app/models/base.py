import uuid
from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, String

from app.core.database import Base


def get_utc_now() -> datetime:
    return datetime.now(UTC)


class AuditBase(Base):
    """Abstract base model with UUID primary key and audit timestamps."""
    __abstract__ = True

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    created_at = Column(
        DateTime(timezone=True),
        default=get_utc_now,
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=get_utc_now,
        onupdate=get_utc_now,
        nullable=False
    )
