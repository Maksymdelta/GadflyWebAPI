"""empty message

Revision ID: 8c7d2b6f9e1e
Revises: 09ad3b11398d
Create Date: 2016-04-21 00:08:09.072894

"""

# revision identifiers, used by Alembic.
revision = '8c7d2b6f9e1e'
down_revision = '09ad3b11398d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer_choice', sa.Column('answer', sa.String(), nullable=True))
    op.drop_column('answer_choice', 'answer_choice')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer_choice', sa.Column('answer_choice', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('answer_choice', 'answer')
    ### end Alembic commands ###
