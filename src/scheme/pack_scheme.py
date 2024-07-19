from typing import Optional  # Import Optional for optional type hinting
from pydantic import BaseModel  # Import BaseModel from Pydantic for data validation and serialization

class Pack(BaseModel):
    # Optional field for the pack ID, could be None
    id_pack: Optional[int]
    # Field for the name or description of the pack
    name_pack: str
    # Field for the price of the pack
    price_pack: float
    # Field for the first discount on the pack
    first_discount: float
    # Field for the second discount on the pack
    second_discount: float
