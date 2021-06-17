"""empty message

Revision ID: ab3dc8072fdd
Revises: 93b27739be67
Create Date: 2021-06-17 09:56:37.756059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3dc8072fdd'
down_revision = '93b27739be67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('create_date', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column('update_date', sa.DateTime(), nullable=False))
    op.create_foreign_key(None, 'users', 'countries', ['country_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'update_date')
    op.drop_column('users', 'create_date')
    # ### end Alembic commands ###
