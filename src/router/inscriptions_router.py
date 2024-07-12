from fastapi import APIRouter, Depends
from schemas.inscripciones import Inscripciones
from services.inscripciones_services import Inscripciones_services
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_async_session

# RUTAS
router = APIRouter( prefix="/inscripciones", tags=["Inscripciones"])
inscripciones_serv = Inscripciones_services()


# COSULTAR TODAS LAS INSCRIPCIONES
@router.get("/inscripciones/")
async def consultar_inscripciones(db: AsyncSession = Depends(get_async_session)):
    return await inscripciones_serv.consultar_inscripciones(db)


# CONSULTAR UNA INSCRIPCIÓN POR ID
@router.get("/inscripcion/{id}")
async def consultar_una_inscripcion(id:int, db: AsyncSession = Depends(get_async_session)):
    return await inscripciones_serv.consultar_inscripcion_por_id(id, db)


# CONSULTAR INSCRIPCIONES PAGADAS POR ID ALUMNO
@router.get("/inscripciones_pagadas/{id}")
async def consultar_inscripciones_pagas( id:int, boleano: bool, db: AsyncSession = Depends(get_async_session)):
    return await inscripciones_serv.consultar_inscripciones_pagadas(id, boleano, db)


# CREAR UNA NUEVA INSCRIPCIÓN
@router.post("/inscripcion")
async def crear_inscripcion(data:Inscripciones, db: AsyncSession = Depends(get_async_session)):
    return await inscripciones_serv.crear_inscripcion(data, db)


# EDITAR UNA INSCRIPCIÓN
@router.put("/inscripcion/{id}")
async def editar_inscripcion(id: int, data:Inscripciones, db: AsyncSession = Depends(get_async_session)):
    return await inscripciones_serv.editar_inscripcion(id, data, db)


# ELIMINAR INSCRIPCION
@router.delete("/inscripcion/{id}")
async def eliminar_inscripcion(id: int, db: AsyncSession = Depends(get_async_session)):
   return await inscripciones_serv.eliminar_inscripcion(id, db)