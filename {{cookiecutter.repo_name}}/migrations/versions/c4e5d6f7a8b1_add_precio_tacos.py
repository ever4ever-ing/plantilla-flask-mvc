"""add precio to tacos

Revision ID: c4e5d6f7a8b1
Revises: 8f2a1c3b9d0e
Create Date: 2026-03-29

"""

import sqlalchemy as sa
from alembic import op

revision = "c4e5d6f7a8b1"
down_revision = "8f2a1c3b9d0e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "tacos",
        sa.Column("precio", sa.Float(), nullable=False, server_default="0"),
    )


def downgrade():
    op.drop_column("tacos", "precio")
