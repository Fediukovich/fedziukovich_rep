"""initial
Revision ID: 02f7fa162ec1
Revises:
Create Date: 2023-02-28 11:18:05.729522
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf084279c7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=6, scale=2), nullable=False),
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('category')
    # ### end Alembic commands ###