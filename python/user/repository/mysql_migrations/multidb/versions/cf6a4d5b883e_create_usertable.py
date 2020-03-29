"""create usertable

Revision ID: cf6a4d5b883e
Revises: 
Create Date: 2020-03-29 15:55:34.849616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf6a4d5b883e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                        sa.Column("id", sa.Integer, primary_key=True),
                        sa.Column("username", sa.Text),
                        sa.Column("email", sa.Text),
                        sa.Column("fullname", sa.Text),
                        sa.Column("password", sa.Text),
                        sa.Column("password_salt", sa.Text),
                        sa.Column("status", sa.Text)
                    )

def downgrade():
    op.drop_table("users")
