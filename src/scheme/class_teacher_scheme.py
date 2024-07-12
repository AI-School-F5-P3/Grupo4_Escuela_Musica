from typing import Optional
from pydantic import BaseModel

class Class_teacher(BaseModel):

    id_class_teacher : Optional[int]
    class_id:int
    teacher_id:int
    level_id:int
