"""Initial migration

Revision ID: c8a81f54bd9e
Revises: 
Create Date: 2023-05-23 20:32:20.863175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8a81f54bd9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_id', sa.String(length=50), nullable=True),
    sa.Column('is_member', sa.Boolean(), nullable=True),
    sa.Column('display_name', sa.String(length=255), nullable=True),
    sa.Column('picture_url', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('line_id')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_id', sa.String(length=50), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('joined_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['line_id'], ['user.line_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member')
    op.drop_table('user')
    # ### end Alembic commands ###
