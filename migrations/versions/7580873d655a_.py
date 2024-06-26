"""empty message

Revision ID: 7580873d655a
Revises: bc746fd97d94
Create Date: 2024-05-01 16:59:17.387876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7580873d655a'
down_revision = 'bc746fd97d94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
