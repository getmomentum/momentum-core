"""create inference table

Revision ID: fbc3da27ae0c
Revises: cbd8239ae1b7
Create Date: 2024-07-07 21:46:06.677606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection


# revision identifiers, used by Alembic.
revision: str = 'fbc3da27ae0c'
down_revision: Union[str, None] = 'cbd8239ae1b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Get the current engine and inspector
    engine = op.get_bind()
    inspector = reflection.Inspector.from_engine(engine)

    # List of existing tables
    existing_tables = inspector.get_table_names()

    # Check if the 'inference' table already exists
    if 'inference' not in existing_tables:
        # Create the table if it does not exist
        # ### commands auto generated by Alembic - please adjust! ###
        op.create_table('inference',
        sa.Column('key', sa.Text(), nullable=False),
        sa.Column('inference', sa.Text(), nullable=True),
        sa.Column('hash', sa.Text(), nullable=True),
        sa.Column('explanation', sa.Text(), nullable=True),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('key', 'project_id')
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inference')
    # ### end Alembic commands ###
