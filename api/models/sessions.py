import uuid

from pydantic.v1 import UUID4
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from api.db.database import Base

class SessionsModel(Base):
    __tablename__ = "sessions"
    __table_args__ = {"extend_existing": True}

    id : Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mentor_id : Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    mentee_id : Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    scheduled_at: Mapped[DateTime] = mapped_column(DateTime)
    status : Mapped[String] = mapped_column(String(25))
    created_at : Mapped[DateTime] = mapped_column(DateTime)

class ScheduledSessionsView(Base):
    __tablename__ = "view_scheduled_sessions"
    __table_args__ = {"extend_existing": True}

    session_id : Mapped[UUID4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scheduled_at : Mapped[DateTime] = mapped_column(DateTime)
    status : Mapped[String] = mapped_column(String(25))
    mentor_name : Mapped[String] = mapped_column(String(255))
    mentee_name : Mapped[String] = mapped_column(String(255))