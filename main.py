from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.user_connection import UserConnection #importamos la conexion de models a UserConnection
from schema.alumno_schema import AlumnoSchema
from schema.clase_schema import ClaseSchema
from schema.profesor_schema import ProfesorSchema

"""
En este archivo importamos los schema de cada tabla y trabamos los datos
que debe devolvernos la clase UserConnection.

Como buena práctica, con la calse Response de fast API y la biblioteca Starlette
le informaremos a fastAPI que respuestas (por ejemplo: status 200, 201, 204 et...) 
debería estar esperando de cada una de las rutas creadas.
Response 200: Por defecto todas las rutas esperan un código 200 pero se lo aclaramos. Singnifica ok.
Response 201: Informa que se ha creado un nuevo registro.
Response 204: Indica que se ha realizado una acción correctamente pero no se devuelve contenido.
"""

app = FastAPI() #se inicializa la app
conn = UserConnection() #instanciamos objeto conn


#RUTAS TABLA ALUMNO

@app.get("/mostrar/alumno", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def root():
    items = []#con esta lista hacemos que la terminal nos devuelva la info en formato de tuplas
    for data in conn.read_all_alumno():
        dictionary = {}#con este diccionario le damos formato a nuestros datos mostrados en la api
        dictionary["alumno_id"] = data[0]
        dictionary["nombre"] = data[1]
        dictionary["apellido"] = data[2]
        dictionary["edad"] = data[3]
        dictionary["telefono"] = data[4]
        dictionary["email"] = data[5]
        dictionary["es_familiar"] = data[6]
        items.append(dictionary)
    return items
  
    
@app.get("/mostrar/alumno/{id}", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def get_one_alumno(id:int):
    dictionary = {}#con esto le damos formato a lo que nos devuelve la bd
    data = conn.read_one_alumno(id)#con este método le indicamos a la api que nos retorne el mismo valor de id que se esta consultando
    dictionary["alumno_id"] = data[0]
    dictionary["nombre"] = data[1]
    dictionary["apellido"] = data[2]
    dictionary["edad"] = data[3]
    dictionary["telefono"] = data[4]
    dictionary["email"] = data[5]
    dictionary["es_familiar"] = data[6]
    return dictionary
    #return id


@app.post("/agregar/alumno",status_code=HTTP_201_CREATED) #se crea un decorador con la ruta post
def insert(data:AlumnoSchema):
    data = data.model_dump() #el método model_dump es el equivalente a dict
    data.pop("alumno_id")#esto es para decirle a la API que no nos devuelva el id
    conn.write_alumno(data)#esto escribirá en la db (ejecutará la sentencia SQL INSERT)
    return Response (status_code=HTTP_201_CREATED)


@app.put("/modificar/alumno/{alumno_id}",status_code=HTTP_204_NO_CONTENT)#el método put esta asociado a la actualización de datos en los verbos HTTP
def update(data:AlumnoSchema,alumno_id:str):#como el id esta siendo pasado como url hay que crear un diccionario
    data = data.model_dump()
    data['alumno_id'] = alumno_id
    #print(data)     
    conn.update_alumno(data)
    return Response (status_code=HTTP_204_NO_CONTENT)


@app.delete("/eliminar/alumno/{id}",status_code=HTTP_204_NO_CONTENT) #ruta para eliminar registros de la tabla alumno
def delete(id:int):
    conn.delete_alumno(id)
    return Response (status_code=HTTP_204_NO_CONTENT)



#RUTAS TABLA PROFESOR

@app.get("/mostrar/profesor", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def root():
    items = []#con esta lista hacemos que la terminal nos devuelva la info en formato de tuplas
    for data in conn.read_all_profesor():
        dictionary = {}#con este diccionario le damos formato a nuestros datos mostrados en la api
        dictionary["profesor_id"] = data[0]
        dictionary["nombre"] = data[1]
        # dictionary["apellido"] = data[2]
        # dictionary["edad"] = data[3]
        # dictionary["telefono"] = data[4]
        # dictionary["email"] = data[5]
        items.append(dictionary)
    return items
    
    
@app.get("/mostrar/profesor/{id}", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def get_one_profesor(id:int):
    dictionary = {}#con esto le damos formato a lo que nos devuelve la bd
    data = conn.read_one_profesor(id)#con este método le indicamos a la api que nos retorne el mismo valor de id que se esta consultando
    dictionary["profesor_id"] = data[0]
    dictionary["nombre"] = data[1]
    # dictionary["apellido"] = data[2]
    # dictionary["edad"] = data[3]
    # dictionary["telefono"] = data[4]
    # dictionary["email"] = data[5]
    # dictionary["es_familiar"] = data[6]
    return dictionary
    #return id


@app.post("/agregar/profesor",status_code=HTTP_201_CREATED) #se crea un decorador con la ruta post
def insert(data:ProfesorSchema):
    data = data.model_dump() #el método model_dump es el equivalente a dict
    data.pop("profesor_id")#esto es para decirle a la API que no nos devuelva el id
    conn.write_profesor(data)#esto escribirá en la db (ejecutará la sentencia SQL INSERT)
    return Response (status_code=HTTP_201_CREATED)


@app.put("/modificar/profesor/{profesor_id}",status_code=HTTP_204_NO_CONTENT)#el método put esta asociado a la actualización de datos en los verbos HTTP
def update(data:ProfesorSchema,profesor_id:str):#como el id esta siendo pasado como url hay que crear un diccionario
    data = data.model_dump()
    data['profesor_id'] = profesor_id
    #print(data)     
    conn.update_profesor(data)
    return Response (status_code=HTTP_204_NO_CONTENT)


@app.delete("/eliminar/profesor/{id}",status_code=HTTP_204_NO_CONTENT) #ruta para eliminar registros de la tabla profesor
def delete(id:int):
    conn.delete_profesor(id)
    return Response (status_code=HTTP_204_NO_CONTENT)



#RUTAS TABLA CLASE

@app.get("/mostrar/clase", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def root():
    items = []#con esta lista hacemos que la terminal nos devuelva la info en formato de tuplas
    for data in conn.read_all_clase():
        dictionary = {}#con este diccionario le damos formato a nuestros datos mostrados en la api
        dictionary["clase_id"] = data[0]
        dictionary["alumno_id"] = data[1]
        dictionary["nivel"] = data[2]
        dictionary["instrumento"] = data[3]
        dictionary["mes_anio"] = data[4]
        dictionary["profesor_id"] = data[5]
        items.append(dictionary)
    return items
    
  
@app.get("/mostrar/clase/{id}", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def get_one_clase(id:int):
    dictionary = {}#con esto le damos formato a lo que nos devuelve la bd
    data = conn.read_one_clase(id)#con este método le indicamos a la api que nos retorne el mismo valor de id que se esta consultando
    dictionary["clase_id"] = data[0]
    dictionary["alumno_id"] = data[1]
    dictionary["nivel"] = data[2]
    dictionary["instrumento"] = data[3]
    dictionary["mes_anio"] = data[4]
    dictionary["profesor_id"] = data[5]
    return dictionary
    #return id


@app.post("/agregar/clase",status_code=HTTP_201_CREATED) #se crea un decorador con la ruta post
def insert(data:ClaseSchema):
    data = data.model_dump() #el método model_dump es el equivalente a dict
    data.pop("clase_id")#esto es para decirle a la API que no nos devuelva el id
    conn.write_clase(data)#esto escribirá en la db (ejecutará la sentencia SQL INSERT)
    return Response (status_code=HTTP_201_CREATED)


@app.put("/modificar/clase/{clase_id}",status_code=HTTP_204_NO_CONTENT)#el método put esta asociado a la actualización de datos en los verbos HTTP
def update(data:ClaseSchema,clase_id:str):#como el id esta siendo pasado como url hay que crear un diccionario
    data = data.model_dump()
    data['clase_id'] = clase_id
    #print(data)     
    conn.update_clase(data)
    return Response (status_code=HTTP_204_NO_CONTENT)


@app.delete("/eliminar/clase/{id}",status_code=HTTP_204_NO_CONTENT) #ruta para eliminar registros de la tabla user
def delete(id:int):
    conn.delete_clase(id)
    return Response (status_code=HTTP_204_NO_CONTENT)