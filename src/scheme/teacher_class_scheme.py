from typing import Optional
from pydantic import BaseModel

class TeacherClass(BaseModel):

    id_class_teacher : Optional[int]
    id_class:int
    id_teacher:int
    id_level:int

class Config:
    from_attributes = True