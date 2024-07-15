from datetime import date
from typing import Optional
from pydantic import BaseModel


class Inscription(BaseModel):

    id_inscription : Optional[int]
    id_class_teacher:int
    id_student:int
    price_class:float
    discount_inscription:float
    family_discount:float
    price_with_discount:float
    paid: bool= False
    inscription_date: date
    end_date: date


     