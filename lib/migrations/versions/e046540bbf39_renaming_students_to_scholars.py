"""Renaming students to scholars

Revision ID: e046540bbf39
Revises: 791279dd0760
Create Date: 2023-05-31 17:05:39.016029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e046540bbf39'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')