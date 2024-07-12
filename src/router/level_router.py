from fastapi import APIRouter, Depends
from schemas.niveles import Niveles
from services.niveles_services import Niveles_services
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_async_session


router = APIRouter(prefix="/niveles", tags=["niveles"])
niveles_service = Niveles_services()


# COSULTAR TODOS LOS NIVELES
@router.get("/niveles/")
async def consultar_niveles(db: AsyncSession = Depends(get_async_session)):
    return await niveles_service.consultar_niveles(db)


# CONSULTAR UN NIVEL POR EL NOMBRE
@router.get('/nivel/{nombre}')# nombre es el parámetro de ruta que es pero recibir cuanod el usuario acceda  a esta url
async def consultar_nivel_por_nombre(nombre: str, db: AsyncSession = Depends(get_async_session)):
    return await niveles_service.consultar_nivel(db, nombre)


# AGREGAR UN NUEVO NIVEL
@router.post("/niveles/")
async def agregar_nivel(data: Niveles, db: AsyncSession = Depends(get_async_session)):
    return await niveles_service.agregar_nivel(db, data)


# EDITAR UN NIVEL
@router.put('/niveles/{nombre}')
async def editar_nivel(data: Niveles, nombre: str, db: AsyncSession = Depends(get_async_session)):
    return await niveles_service.editar_nivel(db, nombre, data)




