"""empty message

Revision ID: d3a706c1d86a
Revises: 4630979eb3d1
Create Date: 2022-03-17 13:57:09.558366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a706c1d86a'
down_revision = '4630979eb3d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sci_name', sa.String(length=100), nullable=False),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('diet', sa.String(length=250), nullable=True),
    sa.Column('habitat', sa.String(length=250), nullable=True),
    sa.Column('lifespan', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('sci_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animal')
    # ### end Alembic commands ###
