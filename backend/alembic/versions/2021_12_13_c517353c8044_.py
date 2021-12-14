"""

Revision ID: c517353c8044
Revises: 0db5f99ab1af
Create Date: 2021-12-13 03:43:00.866493

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

import src.models.fields


# revision identifiers, used by Alembic.
revision = 'c517353c8044'
down_revision = '0db5f99ab1af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utilization',
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('deleted_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('id', src.models.fields.uuid.UUID(length=16), nullable=False),
    sa.Column('utilized', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('claim_line_items_id', src.models.fields.uuid.UUID(length=16), nullable=False),
    sa.ForeignKeyConstraint(['claim_line_items_id'], ['claim_line_items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utilization')
    # ### end Alembic commands ###