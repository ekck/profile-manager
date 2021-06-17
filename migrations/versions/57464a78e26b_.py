"""empty message

Revision ID: 57464a78e26b
Revises: ab3dc8072fdd
Create Date: 2021-06-17 10:01:50.750565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57464a78e26b'
down_revision = 'ab3dc8072fdd'
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
