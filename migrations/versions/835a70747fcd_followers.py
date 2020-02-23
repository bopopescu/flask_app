"""followers

Revision ID: 835a70747fcd
Revises: 836e8ec825c8
Create Date: 2020-02-16 14:53:08.122820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '835a70747fcd'
down_revision = '836e8ec825c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###