"""add descripcion to tacos

Revision ID: b1d4a45d49e6
Revises: c4e5d6f7a8b1
Create Date: 2026-03-29

"""

import sqlalchemy as sa
from alembic import op

revision = "b1d4a45d49e6"
down_revision = "c4e5d6f7a8b1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "tacos",
        sa.Column(
            "descripcion",
            sa.String(length=255),
            nullable=False,
            server_default="",
        ),
    )


def downgrade():
    op.drop_column("tacos", "descripcion")
