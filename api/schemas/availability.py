from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class AvailabilitySlotRead(BaseModel):
    id: int
    mentor_id: UUID
    start_time: datetime
    end_time: datetime
    timezone : str

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode
