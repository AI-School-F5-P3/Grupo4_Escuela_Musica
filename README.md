# 🎵 Escuela de Música Armonía API + SQL 🎵

## Descripción del Proyecto

La Escuela de Música Armonía es una pequeña escuela de música que ha tenido más éxito del esperado. Mar, la dueña de la escuela, necesita una solución para gestionar los alumnos y las cuentas de la escuela de una manera más eficiente y sin errores. Este proyecto tiene como objetivo desarrollar una API RESTful y una base de datos SQL para gestionar toda la información de la escuela de manera robusta y escalable.

## 📋 Planteamiento

### Profesores

- Mar
- Flor
- Nayara
- Marifé
- Álvaro
- Nieves
- Sofía

### Clases e Instructores

- **Piano**: Mar, Flor, Álvaro, Marifé y Nayara 
- **Guitarra**: Mar y Flor
- **Batería**: Mar 
- **Violín**: Nayara 
- **Canto**: Marifé 
- **Flauta**: Mar 
- **Saxofón**: Nieves 
- **Clarinete**: Nieves 
- **Percusión**: Sofía 
- **Bajo**: Nayara

### Precios

- **Piano, Guitarra, Batería, Flauta**: 35€ (con descuentos del 50% y 75% para segunda y tercera clases respectivamente)
- **Resto de clases**: 40€ (con descuentos del 50% y 75% para segunda y tercera clases respectivamente)

### Niveles

- **Piano**: Cero, Iniciación, Medio, Avanzado 
- **Guitarra**: Iniciación, Medio 
- **Batería**: Iniciación, Medio, Avanzado
- **Flauta**: Iniciación, Medio 
- **Bajo**: Iniciación, Medio
- **Resto de clases**: Un único nivel

## 🚀 Tecnologías Utilizadas

- ![Python](https://img.shields.io/badge/Python-FFD43B?style=flat&logo=python&logoColor=darkgreen) FastAPI, 
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white) PostgreSQL, 
- ![pgAdmin](https://img.shields.io/badge/pgAdmin-336791?style=flat&logo=pgadmin&logoColor=white)  pgadmin…
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) Git, GitHub
- ![Swagger](https://img.shields.io/badge/Swagger-000000?style=flat&logo=swagger&logoColor=white) Swagger…
- ![Jira](https://img.shields.io/badge/Jira-0079BF?style=flat&logo=jira&logoColor=white) Jira…
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-00758F?style=flat&logo=sqlalchemy&logoColor=white) SQLAlchemy, cursor, psycopg2, asyncpg…

#Próximamente:
- ![Testing](https://img.shields.io/badge/Testing-007ACC?style=flat&logo=testing-library&logoColor=white) pytest, unittest…

## 📑 Niveles de Entrega

### Nivel Esencial

- ✅ Mínimo 3 tablas relacionadas entre sí
- ✅ Esquema UML de la estructura de tablas
- ✅ API REST con operaciones CRUD
- 🟡 Tests completos pasados con éxito  - to be implemented.
- ✅ Documentación completa en MarkDown 
- ✅ Tablero Kanban con historias de usuario y un SCRUM bien ejecutado 
- ✅ Datos sensibles externalizados 
- ✅ Trazabilidad con logs 
- ✅ Control de excepciones 

### Nivel Medio

- 📈 Estructura compleja de tablas con distintos tipos de relaciones entre sí
- 📄 Documentación en Swagger y/o Notion
- 🛑 Control de excepciones, con mensajes específicos de error y devolución adecuada de códigos HTTP
- 📊 Posibilidad de descargar los datos relevantes en formato CSV - to be implemented
- 📆 Que la inscripción en las clases de la escuela esté segregado por meses - to be implemented

### Nivel Avanzado - to be implemented

- 🔒 API securizada con JWT
- 🏷️ Gestión de cabeceras para sesiones
- 🛂 Gestión de permisos por roles

### Nivel Experto - to be implemented

- 🤖 Bot de Telegram para gestionar los datos
- 🐋 API Dockerizada
- ☁️ Despliegue en Cloud

## 📦 Instalación y Configuración

1. Clona el repositorio:
    ```bash
    git clone https://github.com/AI-School-F5-P3/Grupo4_Escuela_Musica.git
    cd Grupo4_Escuela_Musica
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configura las variables de entorno en el archivo `.env`:
    ```bash
    DB_HOST=<host>
    DB_NAME=<database_name>
    DB_USER=<user>
    DB_PASS=<password>
    ```

4. Ejecuta las migraciones para crear las tablas en la base de datos:
    ```bash
    alembic upgrade head
    ```

5. Inicia el servidor:
    ```bash
    uvicorn main:app --reload
    ```

## 📋 Endpoints de la API

- **GET** `/student`: Obtener todos los student
- **POST** `/student`: Crear un nuevo alumno
- **GET** `/student/{id}`: Obtener un alumno por ID
- **PUT** `/student/{id}`: Actualizar un alumno por ID
- **DELETE** `/student/{id}`: Eliminar un alumno por ID
- (más endpoints para profesores, clases, facturas, etc.)

## 📄 Esquema UML de la Base de Datos

![UML Diagram](path/to/uml_diagram.png)

## ⚙️ Testing - To be implemented

Para ejecutar los tests, usa el siguiente comando:
```bash
pytest
