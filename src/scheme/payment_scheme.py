from datetime import date
from typing import Optional
from pydantic import BaseModel

class Payment(BaseModel):
    payment_id:Optional[int]
    inscription_id:int
    payment_day:date
