from pydantic import BaseModel
from typing import Optional

"""
A traves de UserSchema generamos los Schemas que estaremos utilizando como 
estructura para ingresar los datos a la base de datos
"""
class ClaseSchema(BaseModel):
    clase_id: Optional[int] = None #dado que nuestro id se estará autogenerando, con lo cual este dato no lo estaremos pasando
    alumno_id: str
    fecha_inicio: str
    fecha_fin: str
    nivel:str
    instrumento: str

    

    