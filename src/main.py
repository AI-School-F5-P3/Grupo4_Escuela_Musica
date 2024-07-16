from router import teacher_class_router
from router import inscription_router
from router import teacher_router
from router import student_router
from router import level_router
from router import class_router
from router import pack_router
from csv_export import csv_export_router
from fastapi import FastAPI
from decouple import config
import uvicorn
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

# endpoints incorporated in API
app.include_router(teacher_class_router.router)
app.include_router(inscription_router.router)
app.include_router(teacher_router.router)
app.include_router(student_router.router)
app.include_router(level_router.router)
app.include_router(class_router.router)
app.include_router(pack_router.router)
app.include_router(csv_export_router.router)



# function to create all tables in the database if they do not exist
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # Ensure the database tables are created using Base - declarative_base instance


# uvicorn app:main --host localhost --port 5000 --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
