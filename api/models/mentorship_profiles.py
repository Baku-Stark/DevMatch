import uuid

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from api.db.database import Base

class MentorshipProfiles(Base):
    __tablename__ = "mentorship_profiles"
    __table_args__ = {"extend_existing": True}

    id : Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    bio : Mapped[String] = mapped_column(String, nullable=False)
    experience_level : Mapped[String] = mapped_column(String(25), nullable=False)
    uts_user_id : Mapped[UUID] = mapped_column(ForeignKey("user_tech_stacks.user_id"))
    uts_tech_stack_id : Mapped[Integer] = mapped_column(ForeignKey("user_tech_stacks.tech_stacks_id"))

class MentorProfileView(Base):
    __tablename__ = "view_mentor_profiles"
    __table_args__ = {"extend_existing": True}

    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    mentor_name: Mapped[String] = mapped_column(String(255))
    experience_level: Mapped[String] = mapped_column(String(25))
    bio: Mapped[String] = mapped_column(String)
    tech_stack_ids: Mapped[list[Integer]] = mapped_column(ARRAY(Integer))
    tech_stack_names: Mapped[list[String]] = mapped_column(ARRAY(String))
