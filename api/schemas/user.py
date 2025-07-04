from uuid import UUID
from datetime import datetime

from typing import Annotated
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: Annotated[str, Field(
        description="Nome do usuário",
        examples=["Baku-Stark"],
        max_length=255
    )]
    email: Annotated[str, Field(
        description="Email do usuário",
        examples=["email@example.com"],
        max_length=255
    )]
    role: Annotated[str, Field(
        description="Atuação do usuário (Mentor ou Aluno)",
        examples=["mentor", "mentee"],
        max_length=20
    )]
    avatar_url: Annotated[str, Field(
        description="Icon do usuário",
        examples=["https://img.url/user.png"]
    )]

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: UUID
    created_at : datetime
    updated_at : datetime

    class Config:
        from_attributes = True