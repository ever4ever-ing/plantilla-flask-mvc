"""tacos inicial

Revision ID: 8f2a1c3b9d0e
Revises:
Create Date: 2026-03-29

"""

import sqlalchemy as sa
from alembic import op

revision = "8f2a1c3b9d0e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tacos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("tacos")
