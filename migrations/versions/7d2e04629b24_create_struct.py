"""create struct

Revision ID: 7d2e04629b24
Revises: 
Create Date: 2021-05-19 19:22:05.346277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d2e04629b24'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reaction',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('team_id', sa.String(), nullable=False),
    sa.Column('app_id', sa.String(), nullable=False),
    sa.Column('event_id', sa.String(), nullable=False),
    sa.Column('voteder', sa.String(), nullable=False),
    sa.Column('rateder', sa.String(), nullable=False),
    sa.Column('event', sa.String(), nullable=False),
    sa.Column('channel', sa.String(), nullable=False),
    sa.Column('event_datetime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('event_id'),
    sa.UniqueConstraint('event_id')
    )
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('reaction')
    # ### end Alembic commands ###
