from typing import Optional
from pydantic import BaseModel

class Pack(BaseModel):
    
    id_pack:Optional[int]
    pack:str
    price_pack:float
    first_discount:float
    second_discount:float