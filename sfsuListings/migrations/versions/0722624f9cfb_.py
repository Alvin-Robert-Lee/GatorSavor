"""empty message

Revision ID: 0722624f9cfb
Revises: 
Create Date: 2018-12-04 00:07:38.265036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0722624f9cfb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('AdminName', sa.String(length=30), nullable=False),
    sa.Column('password_hash', sa.String(length=96), nullable=False),
    sa.PrimaryKeyConstraint('AdminName'),
    sa.UniqueConstraint('AdminName')
    )
    op.create_table('messages',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sentFrom', sa.String(length=30), nullable=False),
    sa.Column('sentTo', sa.String(length=30), nullable=False),
    sa.Column('postId', sa.INTEGER(), nullable=False),
    sa.Column('message', sa.String(length=300), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('posts',
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('author', sa.String(length=80), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.Column('image', sa.BLOB(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('category', sa.String(length=80), nullable=False),
    sa.Column('approval', sa.String(length=20), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('name', 'author', 'price', 'id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('registered_user',
    sa.Column('UserName', sa.String(length=30), nullable=False),
    sa.Column('password_hash', sa.String(length=96), nullable=False),
    sa.PrimaryKeyConstraint('UserName'),
    sa.UniqueConstraint('UserName')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registered_user')
    op.drop_table('posts')
    op.drop_table('messages')
    op.drop_table('admin')
    # ### end Alembic commands ###
