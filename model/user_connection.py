import psycopg

"""
A traves de la clase UserConnection nos conectamos a la base de datos y
realizamos las peticiones pertinentes (get, post, delete, update) 
"""

class UserConnection(): #creamos la clase UserConnection para realizar la conexión con la bd
    conn= None
    
    def __init__(self):#Constructor para inicial la conexión con la bd
        try:
            self.conn = psycopg.connect("dbname=escuela_armonia user=test password=123 host=localhost port=5432") #esto es igual a la conexión de nuestra bd
        except psycopg.OperationalError as err:
            print(err) 
            self.conn.close()#en el caso de que haya algún error de conexión con la bd el método self.conn cerrará la bd
    
    def read_all_alumno(self):#nos permitirá leer todos los datos desde nuestra db a nuestra api
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM "alumno"
                               """)
            return data.fetchall()
        
    def read_one_alumno(self,alumno_id:int):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "alumno" WHERE alumno_id = %s
            """, (alumno_id,))
            return data.fetchone()

    
    def write_alumno(self, data):#función para escribir dentro de la bd
        with self.conn.cursor() as cur: #dentro de with si algo falla la bd se cerrará
            cur.execute("""
                INSERT INTO "alumno"(nombre,apellido, edad, telefono, email, es_familiar) VALUES (%(nombre)s,%(apellido)s,%(edad)s,%(telefono)s,%(email)s,%(es_familiar)s)
                """,data)
        self.conn.commit()#para confirmar al método conn que deseamos introducir los datos
                        
    def update_alumno(self, data):
        with self.conn.cursor() as curr:
            curr.execute("""
                UPDATE "alumno" SET nombre = %(nombre)s, apellido = %(apellido)s, edad = %(edad)s, telefono = %(telefono)s, email = %(email)s, es_familiar = %(es_familiar)s WHERE alumno_id = %(alumno_id)s
            """,data)#este data no es una tupla, sino que es un diccionario, con lo cual no se colocan parantesis aquí (en el data)
        self.conn.commit()


    def delete_alumno(self,alumno_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "alumno" WHERE alumno_id = %s
            """,(alumno_id,))
        self.conn.commit()#La sentencia delete necesita el self.conn.commit() para confirmar que estamos realizando una modificación en la bd    

    def __def__(self):#Desctructor para que la conexion se cierre luego de finalizada la sesión
        self.conn.close()
