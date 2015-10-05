"""init database

Revision ID: 44b17f87c90d
Revises: None
Create Date: 2015-10-05 12:56:31.603541

"""

# revision identifiers, used by Alembic.
revision = '44b17f87c90d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    category_table = op.create_table(
                            'category',
                            sa.Column('id', sa.Integer, primary_key=True),
                            sa.Column('category', sa.String(120)))

    op.create_table(
            'ingredient',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('ingredient', sa.String(120)),
            sa.Column('person', sa.String(120)),
            sa.Column('category_id', sa.Integer, sa.ForeignKey('category.id')),
            sa.Column('salad_id', sa.Integer))


    op.bulk_insert(category_table,
            [
                {"category":"Greens"},
                {"category":"Protein"},
                {"category":"Veggies"},
                {"category":"Dressing"},
                {"category":"Other"}
            ])


def downgrade():
    op.drop_table('ingredient')
    op.drop_table('category')

