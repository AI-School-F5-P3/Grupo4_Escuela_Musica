import psycopg

"""
A traves de la clase UserConnection nos conectamos a la base de datos y
realizamos las peticiones pertinentes (get, post, delete, update) 
"""

class UserConnection(): #creamos la clase UserConnection para realizar la conexión con la bd
    conn= None
    
    def __init__(self):#Constructor para inicial la conexión con la bd
        try:
            self.conn = psycopg.connect("dbname=escuela_armonia user=postgres password=5678 host=localhost port=5432") #esto es igual a la conexión de nuestra bd
        except psycopg.OperationalError as err:
            print(err) 
            self.conn.close()#en el caso de que haya algún error de conexión con la bd el método self.conn cerrará la bd
    
    
    #TABLA ALUMNO

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

    
    #TABLA PROFESOR

    def read_all_profesor(self):#nos permitirá leer todos los datos desde nuestra db a nuestra api
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM "profesor"
                               """)
            return data.fetchall()
        
    def read_one_profesor(self,profesor_id:int):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "profesor" WHERE profesor_id = %s
            """, (profesor_id,))
            return data.fetchone()

    
    def write_profesor(self, data):#función para escribir dentro de la bd
        with self.conn.cursor() as cur: #dentro de with si algo falla la bd se cerrará
            cur.execute("""
                INSERT INTO "profesor"(nombre) VALUES (%(nombre)s)
                """,data)
        self.conn.commit()#para confirmar al método conn que deseamos introducir los datos
                        
    def update_profesor(self, data):
        with self.conn.cursor() as curr:    
            curr.execute("""
                UPDATE "profesor" SET nombre = %(nombre)s WHERE profesor_id = %(profesor_id)s
            """,data)#este data no es una tupla, sino que es un diccionario, con lo cual no se colocan parantesis aquí (en el data)
        self.conn.commit()


    def delete_profesor(self,profesor_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "profesor" WHERE profesor_id = %s
            """,(profesor_id,))
        self.conn.commit()#La sentencia delete necesita el self.conn.commit() para confirmar que estamos realizando una modificació 

    
    #TABLA CLASE

    def read_all_clase(self):#nos permitirá leer todos los datos desde nuestra db a nuestra api
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM "clase"
                               """)
            return data.fetchall()
        
    def read_one_clase(self,clase_id:int):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "clase" WHERE clase_id = %s
            """, (clase_id,))
            return data.fetchone()

    
    def write_clase(self, data):#función para escribir dentro de la bd
        with self.conn.cursor() as cur: #dentro de with si algo falla la bd se cerrará
            cur.execute("""
                INSERT INTO "clase"(alumno_id,fecha_inicio, fecha_fin, nivel, instrumento) VALUES (%(alumno_id)s,%(fecha_inicio)s,%(fecha_fin)s,%(nivel)s,%(instrumento)s)
                """,data)
        self.conn.commit()#para confirmar al método conn que deseamos introducir los datos
                        
    def update_clase(self, data):
        with self.conn.cursor() as curr:    
            curr.execute("""
                UPDATE "clase" SET alumno_id = %(alumno_id)s, fecha_inicio = %(fecha_inicio)s, fecha_fin = %(fecha_fin)s, nivel = %(nivel)s, instrumento = %(instrumento)s WHERE clase_id = %(clase_id)s
            """,data)#este data no es una tupla, sino que es un diccionario, con lo cual no se colocan parantesis aquí (en el data)
        self.conn.commit()


    def delete_clase(self,clase_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "clase" WHERE clase_id = %s
            """,(clase_id,))
        self.conn.commit()#La sentencia delete necesita el self.conn.commit() para confirmar que estamos realizando una modificació 



    def __def__(self):#Desctructor para que la conexion se cierre luego de finalizada la sesión
        self.conn.close()
