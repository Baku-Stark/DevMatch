from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from api.db.database import Base

class TechStacks(Base):
    __tablename__ = "tech_stacks"

    id : Mapped[Integer] = mapped_column(Integer, primary_key=True)
    name : Mapped[String] = mapped_column(String)