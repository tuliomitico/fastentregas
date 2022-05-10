"""Create delivery

Revision ID: 0004
Revises: 0003
Create Date: 2022-05-06 11:50:27.144030

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

from models.delivery import StatusType

# revision identifiers, used by Alembic.
revision = '0004'
down_revision = '0003'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
    sa.Column('id', sa.BigInteger(), nullable=False,autoincrement=True),
    sa.Column('hour', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('telephone', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('shop', sa.Text(), nullable=True),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(choices = StatusType,impl=sa.Integer()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery')
    # ### end Alembic commands ###
