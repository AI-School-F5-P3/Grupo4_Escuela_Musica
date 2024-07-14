from typing import Optional  # Import Optional for optional type hints
from pydantic import BaseModel  # Import BaseModel from Pydantic for data validation

# Define a Pydantic model for Teacher
class Teacher(BaseModel):
    id_teacher: Optional[int]  # Optional integer field for the teacher's ID
    name_teacher: str  # String field for the teacher's name
    surname_teacher: str  # String field for the teacher's surname
    email_teacher: str  # String field for the teacher's email


