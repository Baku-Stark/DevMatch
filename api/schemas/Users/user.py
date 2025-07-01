from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str
    avatar_url: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True

class MentorProfileRead(BaseModel):
    user_id: UUID
    mentor_name: str
    tech_stack: str
    experience_level: str
    bio: str

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2