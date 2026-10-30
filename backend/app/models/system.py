from sqlalchemy import JSON, Column, String, Text

from app.models.base import AuditBase


class SystemAuditLog(AuditBase):
    """
    Immutable system audit log for security, operational events,
    and platform configuration updates.
    """
    __tablename__ = "system_audit_logs"

    event_type = Column(String(64), nullable=False, index=True)
    actor = Column(String(128), nullable=False, default="system")
    details = Column(JSON, nullable=True)
    description = Column(Text, nullable=True)
