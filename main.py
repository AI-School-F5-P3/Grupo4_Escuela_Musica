from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.user_connection import UserConnection #importamos la conexion de models a UserConnection
from schema.user_schema import UserSchema

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


@app.get("/", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def root():
    items = []#con esta lista hacemos que la terminal nos devuelva la info en formato de tuplas
    for data in conn.read_all():
        dictionary = {}#con este diccionario le damos formato a nuestros datos mostrados en la api
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)
    return items
    
    

@app.get("/api/user/{id}", status_code=HTTP_200_OK) #se crea un decorador con la ruta base de la applicación
def get_one(id:int):
    dictionary = {}#con esto le damos formato a lo que nos devuelve la bd
    data = conn.read_one(id)#con este método le indicamos a la api que nos retorne el mismo valor de id que se esta consultando
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    return dictionary
    #return id



@app.post("/api/insert",status_code=HTTP_201_CREATED) #se crea un decorador con la ruta post
def insert(user_data:UserSchema):
    data = user_data.model_dump() #el método model_dump es el equivalente a dict
    data.pop("id")#esto es para decirle a la API que no nos devuelva el id
    conn.write(data)#esto escribirá en la db (ejecutará la sentencia SQL INSERT)
    return Response (status_code=HTTP_201_CREATED)


@app.put("/api/update/{id}",status_code=HTTP_204_NO_CONTENT)#el método put esta asociado a la actualización de datos en los verbos HTTP
def update(user_data:UserSchema,id:int):#como el id esta siendo pasado como url hay que crear un diccionario
    data = user_data.model_dump()
    data["id"] = id
    #print(data)     
    conn.update(data)
    return Response (status_code=HTTP_204_NO_CONTENT)


@app.delete("/api/delete/{id}",status_code=HTTP_204_NO_CONTENT) #ruta para eliminar registros de la tabla user
def delete(id:int):
    conn.delete(id)
    return Response (status_code=HTTP_204_NO_CONTENT)