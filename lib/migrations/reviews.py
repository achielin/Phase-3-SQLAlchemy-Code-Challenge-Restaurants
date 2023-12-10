"""reviews
Revision ID: 9f5a18ec9f1c
Revises: 5c651b7ca401
Create Date: 2023-09-05 09:56:59.959198
"""
from alembic import op
import sqlalchemy as sa



revision = '9f5a18ec9f1c'
down_revision = '5c651b7ca401'
branch_labels = None
depends_on = None


def upgrade():
    
    op.create_table('restaurant_customer',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('customer_id', 'restaurant_id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('star_ratings', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    


def downgrade():
    
    op.drop_table('reviews')
    op.drop_table('restaurant_customer')