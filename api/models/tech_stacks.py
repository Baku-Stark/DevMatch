from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from api.db.database import Base

class TechStacks(Base):
    __tablename__ = "tech_stacks"

    id : Mapped[Integer] = mapped_column(Integer, primary_key=True)
    name : Mapped[String] = mapped_column(String(25))

class UserTechStacks(Base):
    __tablename__ = "user_tech_stacks"
    __table_args__ = {"extend_existing": True}

    users_id : Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    tech_stacks_id : Mapped[Integer] = mapped_column(ForeignKey("tech_stacks.id"), primary_key=True)