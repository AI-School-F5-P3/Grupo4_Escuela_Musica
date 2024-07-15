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
                INSERT INTO "clase" (alumno_id, nivel, instrumento, mes_anio, profesor_id) VALUES (%(alumno_id)s, %(nivel)s, %(instrumento)s, %(mes_anio)s, %(profesor_id)s)
                """,data)
        self.conn.commit()#para confirmar al método conn que deseamos introducir los datos
                        
    def update_clase(self, data):
        with self.conn.cursor() as curr:    
            curr.execute("""
                UPDATE "clase" SET alumno_id = %(alumno_id)s, nivel = %(nivel)s, instrumento = %(instrumento)s, mes_anio = %(mes_anio)s, profesor_id = %(profesor_id)s  WHERE clase_id = %(clase_id)s
            """,data)#este data no es una tupla, sino que es un diccionario, con lo cual no se colocan parantesis aquí (en el data)
        self.conn.commit()


    def delete_clase(self,clase_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "clase" WHERE clase_id = %s
            """,(clase_id,))
        self.conn.commit()#La sentencia delete necesita el self.conn.commit() para confirmar que estamos realizando una modificació 


    #TABLA PACK

    def read_all_pack(self):#nos permitirá leer todos los datos desde nuestra db a nuestra api
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM "pack"
                               """)
            return data.fetchall()
        
    def read_one_pack(self,pack_id:int):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "pack" WHERE pack_id = %s
            """, (pack_id,))
            return data.fetchone()

    
    def write_pack(self, data):#función para escribir dentro de la bd
        with self.conn.cursor() as cur: #dentro de with si algo falla la bd se cerrará
            cur.execute("""
                INSERT INTO "pack"(descripcion, descuento_1, descuento_2, precio) VALUES (%(descripcion)s, %(descuento_1)s, %(descuento_2)s,%(precio)s)
                """,data)
        self.conn.commit()#para confirmar al método conn que deseamos introducir los datos
                        
    def update_pack(self, data):
        with self.conn.cursor() as curr:    
            curr.execute("""
                UPDATE "pack" SET descripcion = %(descripcion)s, descuento_1 = %(descuento_1)s, descuento_2 = %(descuento_2)s, precio = %(precio)s WHERE pack_id = %(pack_id)s
            """,data)#este data no es una tupla, sino que es un diccionario, con lo cual no se colocan parantesis aquí (en el data)
        self.conn.commit()


    def delete_pack(self,pack_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "pack" WHERE pack_id = %s
            """,(pack_id,))
        self.conn.commit()#La sentencia delete necesita el self.conn.commit() para confirmar que estamos realizando una modificació 



    #TABLA FACTURA

    def read_all_factura(self):#nos permitirá leer todos los datos desde nuestra db a nuestra api
        with self.conn.cursor() as cur:
            data = cur.execute("""
                               SELECT * FROM "factura"
                               """)
            return data.fetchall()
        
    def read_one_factura(self,factura_id:int):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "factura" WHERE factura_id = %s
            """, (factura_id,))
            return data.fetchone()

    
    def write_factura(self, data):#función para escribir dentro de la bd
        with self.conn.cursor() as cur: #dentro de with si algo falla la bd se cerrará
            cur.execute("""
                INSERT INTO "factura"(fecha_factura, importe, descuento_familiar, alumno_id, pack_id) VALUES (%(fecha_factura)s, %(importe)s, %(descuento_familiar)s, %(alumno_id)s, %(pack_id)s)
                """,data)
        self.conn.commit()#para confirmar al método conn que deseamos introducir los datos
                        
    def update_factura(self, data):
        with self.conn.cursor() as curr:    
            curr.execute("""
                UPDATE "factura" SET fecha_factura = %(fecha_factura)s, importe = %(importe)s, descuento_familiar = %(descuento_familiar)s, alumno_id = %(alumno_id)s, pack_id = %(pack_id)s WHERE factura_id = %(factura_id)s
            """,data)#este data no es una tupla, sino que es un diccionario, con lo cual no se colocan parantesis aquí (en el data)
        self.conn.commit()


    def delete_factura(self,factura_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "factura" WHERE factura_id = %s
            """,(factura_id,))
        self.conn.commit()#La sentencia delete necesita el self.conn.commit() para confirmar que estamos realizando una modificació 



    def __def__(self):#Desctructor para que la conexion se cierre luego de finalizada la sesión
        self.conn.close()
