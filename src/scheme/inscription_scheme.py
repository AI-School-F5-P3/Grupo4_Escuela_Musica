from datetime import date
from typing import Optional
from pydantic import BaseModel


class Incripciones(BaseModel):

    id_inscripcion : Optional[int]
    clas_teacher_id:int
    student_id:int
    class_price:str
    inscription_discount:float
    family_discount:float
    Discount_price:str
    paid:str
    inscription_date: date