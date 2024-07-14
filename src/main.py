from router import teacher_class_router
from router import inscription_router
from router import teacher_router
# from services.incripcion_automatica_services import ejecutar_funcion_en_hora_especifica
from router import student_router
from router import level_router
from router import class_router
from router import pack_router
# # from router.pagos_router import pagos
from fastapi import FastAPI
from decouple import config
import uvicorn
# from middlewares.error_handler import ErrorHandler # Importamos el manejador de errores
# from auth.auth_config import auth_backend, fastapi_users
# from auth.user import UserCreate, UserRead
from config.db import Base, engine

app = FastAPI(title="Musica Armonia API",description="API para administracion de escuela de musica")



# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth",
#     tags=["Auth"],
# )

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["Auth"],
# )

# app.add_middleware(ErrorHandler)
app.include_router(teacher_class_router.router)
app.include_router(inscription_router.router)
app.include_router(teacher_router.router)
app.include_router(student_router.router)
app.include_router(level_router.router)
app.include_router(class_router.router)
app.include_router(pack_router.router)
# app.include_router(pagos)


# function to create all tables in the database if they do not exist

# Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # Ensure the database tables are created
    # assumes we  have a Base declarative_base instance

'''
# Define la hora y minuto específicos para la ejecución (ejemplo: 15:30)
hora_especifica = 00
minuto_especifico = 00
segundos = 00

# Ejecuta la función en la hora determinada
ejecutar_funcion_en_hora_especifica(hora_especifica, minuto_especifico, segundos)
'''

# uvicorn app:main --host localhost --port 5000 --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
