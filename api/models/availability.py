from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from api.db.database import Base

class AvailabilitySlot(Base):
    __tablename__ = "availability_slots"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    mentor_id = Column(UUID(as_uuid=True), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    timezone = Column(String(50))
