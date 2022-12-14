"""empty message

Revision ID: e56e297e3631
Revises: 4d06cbb48adb
Create Date: 2022-09-22 02:10:38.156926

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e56e297e3631'
down_revision = '4d06cbb48adb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorites', 'people_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'planets_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorites', 'planets_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'people_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
