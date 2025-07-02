from pydantic.v1 import UUID4
from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.db.database import Base

class AvailabilitySlot(Base):
    __tablename__ = "availability_slots"
    __table_args__ = {"extend_existing": True}

    id : Mapped[String] = mapped_column(Integer, primary_key=True)
    mentor_id : Mapped[UUID4] = mapped_column(ForeignKey('users.id'))
    start_time : Mapped[DateTime] = mapped_column(DateTime)
    end_time : Mapped[DateTime] = mapped_column(DateTime)
    timezone : Mapped[String] = mapped_column(String(50))