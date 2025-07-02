import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from api.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String(20), nullable=False)
    avatar_url = Column(String, nullable=False)
    created_at = Column(DateTime)

class MentorProfileView(Base):
    __tablename__ = "view_mentor_profiles"
    __table_args__ = {"extend_existing": True}

    user_id = Column(UUID(as_uuid=True), primary_key=True)
    mentor_name = Column(String(255))
    tech_stack = Column(String(25))
    experience_level = Column(String(25))
    bio = Column(String)
