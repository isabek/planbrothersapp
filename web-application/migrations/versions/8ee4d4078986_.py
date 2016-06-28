"""empty message

Revision ID: 8ee4d4078986
Revises: df10efff3fe0
Create Date: 2016-06-28 13:01:00.722237

"""

# revision identifiers, used by Alembic.
revision = '8ee4d4078986'
down_revision = 'df10efff3fe0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'bros_best_friend_id_fkey', 'bros', type_='foreignkey')
    op.create_foreign_key(None, 'bros', 'bros', ['best_friend_id'], ['id'], ondelete='SET NULL')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bros', type_='foreignkey')
    op.create_foreign_key(u'bros_best_friend_id_fkey', 'bros', 'bros', ['best_friend_id'], ['id'])
    ### end Alembic commands ###
