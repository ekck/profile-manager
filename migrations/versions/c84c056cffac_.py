"""empty message

Revision ID: c84c056cffac
Revises: 06c020cdf7a5
Create Date: 2021-06-20 16:55:55.830599

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c84c056cffac'
down_revision = '06c020cdf7a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('box_number', sa.Integer(), nullable=False),
    sa.Column('postal_code', sa.Integer(), nullable=False),
    sa.Column('town', sa.String(length=20), nullable=False),
    sa.Column('county', sa.String(length=20), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['countries.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dependants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('relationship', sa.String(length=20), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('second_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dependants_first_name'), 'dependants', ['first_name'], unique=False)
    op.create_index(op.f('ix_dependants_last_name'), 'dependants', ['last_name'], unique=False)
    op.create_index(op.f('ix_dependants_second_name'), 'dependants', ['second_name'], unique=False)
    op.add_column(u'countries', sa.Column('m49_code', sa.Integer(), nullable=True))
    op.add_column(u'countries', sa.Column('iso_alpha3', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'countries', ['iso_alpha3'])
    op.create_unique_constraint(None, 'countries', ['m49_code'])
    op.add_column(u'status', sa.Column('name', sa.String(length=60), nullable=True))
    op.drop_index('status', table_name='status')
    op.create_unique_constraint(None, 'status', ['name'])
    op.drop_column(u'status', 'status')
    op.add_column(u'users', sa.Column('date_of_birth', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'users', 'date_of_birth')
    op.add_column(u'status', sa.Column('status', mysql.VARCHAR(length=60), nullable=True))
    op.drop_constraint(None, 'status', type_='unique')
    op.create_index('status', 'status', ['status'], unique=False)
    op.drop_column(u'status', 'name')
    op.drop_constraint(None, 'countries', type_='unique')
    op.drop_constraint(None, 'countries', type_='unique')
    op.drop_column(u'countries', 'iso_alpha3')
    op.drop_column(u'countries', 'm49_code')
    op.drop_index(op.f('ix_dependants_second_name'), table_name='dependants')
    op.drop_index(op.f('ix_dependants_last_name'), table_name='dependants')
    op.drop_index(op.f('ix_dependants_first_name'), table_name='dependants')
    op.drop_table('dependants')
    op.drop_table('contacts')
    # ### end Alembic commands ###
