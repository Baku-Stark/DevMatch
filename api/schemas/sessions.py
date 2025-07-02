from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class SessionsSchema(BaseModel):
    id : UUID
    mentor_id : UUID
    mentee_id : UUID
    scheduled_at : datetime
    status : str

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2

class ScheduledSessionsRead(BaseModel):
    session_id : UUID
    scheduled_at : datetime
    status : str
    mentor_name : str
    mentee_name : str
    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2