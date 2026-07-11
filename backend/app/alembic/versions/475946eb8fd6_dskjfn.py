"""dskjfn

Revision ID: 475946eb8fd6
Revises: 8ea8527c73f8
Create Date: 2026-07-10 13:15:36.497234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '475946eb8fd6'
down_revision: Union[str, None] = '8ea8527c73f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
