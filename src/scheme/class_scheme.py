from typing import Optional
from pydantic import BaseModel

class Clases(BaseModel):
    
    id_clase: Optional[int]
    class_name: str
    pack_id: int