from typing import Optional  # Import Optional for defining optional type hints
from pydantic import BaseModel  # Import BaseModel from Pydantic for data validation and model creation

# Define a Pydantic model for Level
class Level(BaseModel):
    id_level: Optional[int]  # Optional integer field for the level ID
    name_level: str  # String field for the name of the level


