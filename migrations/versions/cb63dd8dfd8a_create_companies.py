"""create companies

Revision ID: cb63dd8dfd8a
Revises: 
Create Date: 2023-07-25 14:02:42.364566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb63dd8dfd8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cnpj', sa.String(length=20), nullable=True),
    sa.Column('cnae', sa.String(length=10), nullable=True),
    sa.Column('company_name', sa.String(length=200), nullable=True),
    sa.Column('fantasy_name', sa.String(length=200), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('companies')
    # ### end Alembic commands ###