from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from api.db.database import Base

class Languages(Base):
    __tablename__ = "languages"

    id : Mapped[Integer] = mapped_column(Integer, primary_key=True)
    language : Mapped[String] = mapped_column(String)