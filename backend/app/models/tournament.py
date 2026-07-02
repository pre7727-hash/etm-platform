import uuid
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.mixins import IdTimestampMixin

class Tournament(IdTimestampMixin, Base):
    __tablename__ = "tournaments"
    game_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("games.id", ondelete="SET NULL"))
    name: Mapped[str] = mapped_column(String(160), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), nullable=False, unique=True, index=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="draft")
    banner_url: Mapped[str | None] = mapped_column(Text)
