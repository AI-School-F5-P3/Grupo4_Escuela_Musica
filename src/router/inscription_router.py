from fastapi import APIRouter, Depends
from scheme.inscription_scheme import Inscription
from service.inscription_service import InscriptionService
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_async_session

# RUTAS
router = APIRouter(tags=["inscription"])
inscription_serv = InscriptionService()


# COSULTAR TODAS LAS inscription
@router.get("/inscriptions/")
async def consult_inscriptions(db: AsyncSession = Depends(get_async_session)):
    return await inscription_serv.consult_inscriptions(db)


# consult insccription dy id
@router.get("/inscription/{id}")
async def consult_inscription_by_id(id:int, db: AsyncSession = Depends(get_async_session)):
    return await inscription_serv.consult_inscription_id(id, db)


# consult inscription PAGADAS POR ID ALUMNO
@router.get("/paid_inscription/{id}")
async def consult_paid_inscription( id:int, bolean: bool, db: AsyncSession = Depends(get_async_session)):
    return await inscription_serv.consult_paid_inscription(id, bolean, db)


# CREAR UNA NUEVA INSCRIPCIÓN
@router.post("/inscription")
async def create_inscription(data:Inscription, db: AsyncSession = Depends(get_async_session)):
    return await inscription_serv.create_new_inscription(data, db)


# EDITAR UNA INSCRIPCIÓN
@router.put("/inscription/{id}")
async def edit_inscription(id: int, data:Inscription, db: AsyncSession = Depends(get_async_session)):
    return await inscription_serv.edit_inscription(id, data, db)


# ELIMINAR inscription
@router.delete("/inscription/{id}")
async def delete_inscription(id: int, db: AsyncSession = Depends(get_async_session)):
   return await inscription_serv.delete_inscription(id, db)