from typing import Optional
from pydantic import BaseModel

class Class(BaseModel):
    
    id_class: Optional[int]
    name_class: str
    id_pack: int