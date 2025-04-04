"""Create phone number for user column

Revision ID: 687d382887e0
Revises: 
Create Date: 2025-03-12 09:45:08.621354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '687d382887e0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(15), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
