from pydantic import BaseModel
from uuid import UUID

class TechStacksRead(BaseModel):
    id : int
    name : str

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2

class UserTechStacksBase(BaseModel):
    users_id : UUID
    tech_stacks_id: int

class UserTechStacksCreate(UserTechStacksBase):
    pass

class UserTechStacksRead(BaseModel):
    users_id: UUID
    tech_stacks_id: int

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2