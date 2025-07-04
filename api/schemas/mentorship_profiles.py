from uuid import UUID
from pydantic import BaseModel


class MentorshipProfilesBase(BaseModel):
    bio : str
    experience_level : str
    uts_user_id : UUID
    uts_tech_stack_id : int

class MentorshipProfilesCreate(MentorshipProfilesBase):
    pass

class MentorshipProfilesRead(MentorshipProfilesBase):
    id : UUID

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2