import uuid
from sqlalchemy import String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from api.db.database import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name : Mapped[String] = mapped_column(String, nullable=False)
    email : Mapped[String] = mapped_column(String, unique=True, nullable=False)
    role : Mapped[String] = mapped_column(String(20), nullable=False)
    avatar_url : Mapped[String] = mapped_column(String, nullable=False)
    created_at : Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at : Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class MentorProfileView(Base):
    __tablename__ = "view_mentor_profiles"
    __table_args__ = {"extend_existing": True}

    user_id : Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    mentor_name : Mapped[String] = mapped_column(String(255))
    tech_stack : Mapped[String] = mapped_column(String(25))
    experience_level : Mapped[String] = mapped_column(String(25))
    bio : Mapped[String] = mapped_column(String)
