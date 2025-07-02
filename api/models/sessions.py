import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from api.db.database import Base

class SessionsModel(Base):
    __tablename__ = "sessions"
    __table_args__ = {"extend_existing": True}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mentor_id = Column(UUID(as_uuid=True), default=uuid.uuid4())
    mentee_id = Column(UUID(as_uuid=True), default=uuid.uuid4())
    scheduled_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(25))
    created_at = Column(DateTime, default=datetime.utcnow)

class ScheduledSessionsView(Base):
    __tablename__ = "view_scheduled_sessions"
    __table_args__ = {"extend_existing": True}

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scheduled_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(25))
    mentor_name = Column(String(255))
    mentee_name = Column(String(255))