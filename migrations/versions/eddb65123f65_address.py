"""address

Revision ID: eddb65123f65
Revises: a5dbde0b11aa
Create Date: 2025-02-14 07:09:40.180563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'eddb65123f65'
down_revision: Union[str, None] = 'a5dbde0b11aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'pickup_address',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'pickup_address',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
