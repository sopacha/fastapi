"""add content column to post table

Revision ID: ad2bb9b543bf
Revises: 138be49a65ce
Create Date: 2025-08-29 12:03:19.916881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad2bb9b543bf'
down_revision: Union[str, Sequence[str], None] = '138be49a65ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
