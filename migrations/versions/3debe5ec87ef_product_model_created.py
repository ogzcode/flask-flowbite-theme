"""Product Model created

Revision ID: 3debe5ec87ef
Revises: 8e156e37740c
Create Date: 2024-09-02 14:50:34.308830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3debe5ec87ef'
down_revision = '8e156e37740c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_description'), ['description'], unique=True)
        batch_op.create_index(batch_op.f('ix_product_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_name'))
        batch_op.drop_index(batch_op.f('ix_product_description'))

    op.drop_table('product')
    # ### end Alembic commands ###
