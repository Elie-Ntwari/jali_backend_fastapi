"""ajout table maison_accueicl

Revision ID: a158c3675f10
Revises: 0cd7567dd0f5
Create Date: 2025-07-24 15:46:36.743050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a158c3675f10'
down_revision: Union[str, Sequence[str], None] = '0cd7567dd0f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_organisations_id'), table_name='organisations')
    op.drop_table('organisations')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organisations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nom', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('adresse', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('telephone', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('date_creation', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('organisations_pkey')),
    sa.UniqueConstraint('email', name=op.f('organisations_email_key'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('ix_organisations_id'), 'organisations', ['id'], unique=False)
    # ### end Alembic commands ###
