from pydantic import BaseModel
from typing import Optional



"""
A traves de UserSchema generamos los Schemas que estaremos utilizando como 
estructura para ingresar los datos a la base de datos
"""
class ClaseSchema(BaseModel):
    clase_id: Optional[int] = None #dado que nuestro id se estará autogenerando, con lo cual este dato no lo estaremos pasando
    alumno_id:int
    nivel:str
    instrumento: str
    mes_anio:str
    profesor_id:int
    
    class Config:
        orm_mode = True

    """Cuando orm_mode está habilitado en un modelo de Pydantic:
    
    Compatibilidad con ORM: Permite que el modelo Pydantic pueda ser inicializado no solo con diccionarios de datos, 
    sino también directamente con instancias de clases ORM. Esto es especialmente útil cuando obtienes datos de la 
    base de datos en forma de objetos ORM y deseas devolverlos como respuestas de API.

    Serialización: Facilita la serialización de las respuestas API directamente desde los modelos ORM. 
    FastAPI puede tomar un objeto de un ORM y convertirlo en una respuesta JSON de forma automática.
    """
    

    