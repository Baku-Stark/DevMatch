from pydantic import BaseModel

class TechStacksRead(BaseModel):
    id : int
    name : str