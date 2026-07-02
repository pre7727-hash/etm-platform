"""initial schema

Revision ID: 202607030001
Revises:
Create Date: 2026-07-03
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "202607030001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table("games", sa.Column("slug", sa.String(length=80), nullable=False), sa.Column("name", sa.String(length=120), nullable=False), sa.Column("cover_url", sa.Text(), nullable=True), sa.Column("is_active", sa.Boolean(), nullable=False), sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.PrimaryKeyConstraint("id"))
    op.create_index(op.f("ix_games_slug"), "games", ["slug"], unique=True)
    op.create_table("organizations", sa.Column("slug", sa.String(length=80), nullable=False), sa.Column("name", sa.String(length=140), nullable=False), sa.Column("logo_url", sa.Text(), nullable=True), sa.Column("description", sa.Text(), nullable=True), sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.PrimaryKeyConstraint("id"))
    op.create_index(op.f("ix_organizations_slug"), "organizations", ["slug"], unique=True)
    op.create_table("user_profiles", sa.Column("supabase_user_id", postgresql.UUID(as_uuid=True), nullable=False), sa.Column("username", sa.String(length=32), nullable=False), sa.Column("display_name", sa.String(length=80), nullable=True), sa.Column("avatar_url", sa.Text(), nullable=True), sa.Column("bio", sa.String(length=280), nullable=True), sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("supabase_user_id", name="uq_user_profiles_supabase_user_id"))
    op.create_index(op.f("ix_user_profiles_supabase_user_id"), "user_profiles", ["supabase_user_id"], unique=False)
    op.create_index(op.f("ix_user_profiles_username"), "user_profiles", ["username"], unique=True)
    op.create_table("teams", sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=True), sa.Column("name", sa.String(length=140), nullable=False), sa.Column("slug", sa.String(length=100), nullable=False), sa.Column("logo_url", sa.Text(), nullable=True), sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], ondelete="SET NULL"), sa.PrimaryKeyConstraint("id"))
    op.create_index(op.f("ix_teams_slug"), "teams", ["slug"], unique=True)
    op.create_table("tournaments", sa.Column("game_id", postgresql.UUID(as_uuid=True), nullable=True), sa.Column("name", sa.String(length=160), nullable=False), sa.Column("slug", sa.String(length=120), nullable=False), sa.Column("status", sa.String(length=32), nullable=False), sa.Column("banner_url", sa.Text(), nullable=True), sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.ForeignKeyConstraint(["game_id"], ["games.id"], ondelete="SET NULL"), sa.PrimaryKeyConstraint("id"))
    op.create_index(op.f("ix_tournaments_slug"), "tournaments", ["slug"], unique=True)
    op.create_table("ai_jobs", sa.Column("user_profile_id", postgresql.UUID(as_uuid=True), nullable=True), sa.Column("workflow", sa.String(length=80), nullable=False), sa.Column("status", sa.String(length=32), nullable=False), sa.Column("input_payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False), sa.Column("output_payload", postgresql.JSONB(astext_type=sa.Text()), nullable=True), sa.Column("error_message", sa.Text(), nullable=True), sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.ForeignKeyConstraint(["user_profile_id"], ["user_profiles.id"], ondelete="SET NULL"), sa.PrimaryKeyConstraint("id"))
    op.create_index(op.f("ix_ai_jobs_status"), "ai_jobs", ["status"], unique=False)
    op.create_index(op.f("ix_ai_jobs_workflow"), "ai_jobs", ["workflow"], unique=False)

def downgrade() -> None:
    op.drop_table("ai_jobs")
    op.drop_table("tournaments")
    op.drop_table("teams")
    op.drop_table("user_profiles")
    op.drop_table("organizations")
    op.drop_table("games")
