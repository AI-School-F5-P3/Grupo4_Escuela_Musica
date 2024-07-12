from typing import Optional
from pydantic import BaseModel

class Teacher(BaseModel):

    id_profesor : Optional[int]
    name_teacher:str
    surname_teacher:str
    email_teacher:str

