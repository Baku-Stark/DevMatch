from pydantic import BaseModel


class LanguagesRead(BaseModel):
    id : int
    language : str