from typing import Optional
from pydantic import BaseModel

class Level(BaseModel):
    id_level:Optional[int]
    name_level:str