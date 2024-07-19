from pydantic import BaseModel
from typing import Optional

"""
A traves de UserSchema generamos los Schemas que estaremos utilizando como 
estructura para ingresar los datos a la base de datos
"""
class PackSchema(BaseModel):
    pack_id: Optional[int] = None #dado que nuestro id se estará autogenerando, con lo cual este dato no lo estaremos pasando
    descripcion: str
    descuento_1: float
    descuento_2: float
    precio: float
    

    class Config:
        orm_mode = True

    