"""empty message

Revision ID: 970e1697977b
Revises: None
Create Date: 2016-04-18 23:20:19.305172

"""

# revision identifiers, used by Alembic.
revision = '970e1697977b'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_article',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('article_text', sa.Text(), nullable=True),
    sa.Column('domain', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_generation_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('questions', postgresql.JSON(), nullable=True),
    sa.Column('question_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('question_text', sa.Text(), nullable=True),
    sa.Column('source_sentence', sa.Text(), nullable=True),
    sa.Column('correct_answer', sa.String(), nullable=True),
    sa.Column('good_question_votes', sa.Integer(), nullable=True),
    sa.Column('bad_question_votes', sa.Integer(), nullable=True),
    sa.Column('news_article_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['news_article_id'], ['news_article.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    op.drop_table('question_generation_request')
    op.drop_table('news_article')
    ### end Alembic commands ###
