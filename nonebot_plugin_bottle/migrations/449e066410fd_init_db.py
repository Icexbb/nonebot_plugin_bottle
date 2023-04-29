"""init_db

Revision ID: 449e066410fd
Revises: 
Create Date: 2023-03-10 14:34:07.064331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "449e066410fd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_bottle_bottle",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("group_id", sa.BigInteger(), nullable=False),
        sa.Column("user_name", sa.String(255), nullable=False),
        sa.Column("group_name", sa.String(255), nullable=False),
        sa.Column("content", sa.JSON(), nullable=False),
        sa.Column("report", sa.Integer(), nullable=False),
        sa.Column("picked", sa.Integer(), nullable=False),
        sa.Column("is_del", sa.Boolean(), nullable=False),
        sa.Column("time", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("nonebot_plugin_bottle_bottle", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_nonebot_plugin_bottle_bottle_user_id"),
            ["user_id", "group_id"],
            unique=False,
        )

    op.create_table(
        "nonebot_plugin_bottle_comment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("user_name", sa.String(255), nullable=False),
        sa.Column("content", sa.String(255), nullable=False),
        sa.Column("time", sa.DateTime(), nullable=False),
        sa.Column("bottle_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "nonebot_plugin_bottle_report",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("bottle_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "bottle_id", name="unique_report"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_bottle_report")
    op.drop_table("nonebot_plugin_bottle_comment")
    with op.batch_alter_table("nonebot_plugin_bottle_bottle", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_nonebot_plugin_bottle_bottle_user_id"))

    op.drop_table("nonebot_plugin_bottle_bottle")
    # ### end Alembic commands ###
