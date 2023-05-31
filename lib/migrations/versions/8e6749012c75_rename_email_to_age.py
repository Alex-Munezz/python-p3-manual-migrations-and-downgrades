"""Rename email to age

Revision ID: 8e6749012c75
Revises: 436710d6b602
Create Date: 2023-05-25 14:02:59.126103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e6749012c75'
down_revision = '436710d6b602'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'email', new_column_name='age')


def downgrade() -> None:
    op.alter_column('scholars', 'age', new_column_name='email')