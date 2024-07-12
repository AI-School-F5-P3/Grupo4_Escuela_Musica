from fastapi import APIRouter, Depends
from services.clases_services import Clases_services
from schemas.clases import Clases
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_async_session



# clases = APIRouter(tags=["clases"])
router = APIRouter( prefix="/classe", tags=["classes"])
clases_service = Clases_services()


@router.get("/clases/")
async def get_clases(db: AsyncSession = Depends(get_async_session)):
    return await clases_service.consultar_clases(db)

@router.get("/clases/{id}")
async def get_clase(id: int, db: AsyncSession = Depends(get_async_session)):
    return await clases_service.consultar_clase_por_id(db, id)

@router.post("/clases/")
async def create_clase(data: Clases, db: AsyncSession = Depends(get_async_session)):
    return await clases_service.agregar_clase(db, data)

@router.put("/clases/{id}")
async def update_clase(id: int, data: Clases, db: AsyncSession = Depends(get_async_session)):
    return await clases_service.editar_clase(db, id, data)

@router.delete("/clases/{id}")
async def delete_clase(id: int, db: AsyncSession = Depends(get_async_session)):
    return await clases_service.borrar_clase(db, id)
'''
# CONSULTAR CLASES
@clases.get('/clases', response_model= List[Clases] )
def consultar_clases() -> List[Clases]:
    result = Clases_services().consultar_clases()
    return result


# CONSULTAR UNA CLASE POR ID
@clases.get('/clase/{id}', response_model= Clases)
def consultar_clase_por_id(id: int) -> Clases:
    result = Clases_services().consultar_clase_por_id(id)
    return result


# AGREGAR UNA NUEVA CLASE
@clases.post("/clases", response_model=dict)
def agregar_clase(clase: Clases)-> dict:
    result = Clases_services().agregar_clase(clase)
    return result


# EDITAR UNA CLASE
@clases.put("/clases/{id}", response_model=dict)
def editar_clase(id: int, data: Clases)-> dict:
    result = Clases_services().editar_clase(id, data)
    return result


# BORRAR UNA CLASE
@clases.delete('/clase/{id}', response_model=dict)
def borrar_clase(id: int) -> dict:
    result = Clases_services().borrar_clase(id)
    return result
'''