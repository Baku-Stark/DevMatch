from typing import List
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

class MentorProfileRead(BaseModel):
    user_id: UUID
    mentor_name: str
    experience_level: str
    bio: str
    tech_stack_ids: List[int]
    tech_stack_names: List[str]

    class Config:
        from_attributes = True