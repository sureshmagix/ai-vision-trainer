"""Initial system audit and bootstrap tables

Revision ID: 0001_initial_bootstrap
Revises: 
Create Date: 2026-10-30 18:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0001_initial_bootstrap'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'system_audit_logs',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('event_type', sa.String(length=64), nullable=False),
        sa.Column('actor', sa.String(length=128), nullable=False),
        sa.Column('details', sa.JSON(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_system_audit_logs_id'), 'system_audit_logs', ['id'], unique=False)
    op.create_index(op.f('ix_system_audit_logs_event_type'), 'system_audit_logs', ['event_type'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_system_audit_logs_event_type'), table_name='system_audit_logs')
    op.drop_index(op.f('ix_system_audit_logs_id'), table_name='system_audit_logs')
    op.drop_table('system_audit_logs')
