from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):

    id_student : Optional[int]
    name_student:str
    surname_student:str
    age_student:str
    email_student:str
    phone_student:str
    family_discount:float
    

    class Config:
        from_attributes = True
