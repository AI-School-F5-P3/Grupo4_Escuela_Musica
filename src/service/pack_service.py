from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from model.pack_model import PackModel
from scheme.pack_scheme import Pack
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy import delete
from logger import Logs

class PackService:
    def __init__(self):
        self.logger= Logs()

    # CONSULTAR TODOS LOS PACKS
    async def consult_packs(self, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(PackModel))).scalars().all()
        self.logger.debug('Consulting all the packs')
        if not result:
            self.logger.warning('No packs found')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no packs yet") 
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UN PACK POR ID
    async def consult_pack_id(self, db: AsyncSession, id):
        async with db.begin():
            result = (await db.execute(select(PackModel).filter(PackModel.id_pack == id))).scalars().all()
        self.logger.debug(f'Consulting pack id: {id}')
        if not result:
            self.logger.warning('No se encontró el pack')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no pack with that id")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))



    # AGREGAR UN NUEVO PACK
    async def add_pack(self, data: Pack, db: AsyncSession):
        async with db.begin():
            pack = (await db.execute(
                select(PackModel).filter(PackModel.id_pack == data.id_pack))).scalars().first()
            if pack:
                self.logger.warning('The pack already exists with this name')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is already a pack with this name")
            new_pack = PackModel(
                name_pack=data.name_pack,
                price_pack=data.price_pack,
                first_discount=data.first_discount,
                second_discount=data.second_discount
            )  # Create a new pack instance
            db.add(new_pack)
            await db.commit()
            self.logger.info("A new pack has been registered")
            return JSONResponse(status_code=201, content={"message": "A new pack has been registered"})


    # EDITAR UN PACK
    async def edit_pack(self, id: int, data: Pack, db: AsyncSession):
        async with db.begin():
            pack = (await db.execute(select(PackModel).filter(PackModel.id_pack == id))).scalars().first()
            if not pack:
                self.logger.warning('The pack to edit was not found')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no pack with that id")
            pack.name_pack = data.name_pack
            pack.price_pack = data.price_pack
            pack.first_discount = data.first_discount
            pack.second_discount = data.second_discount
            await db.commit()
            self.logger.info('The pack has been modified')
            return JSONResponse(status_code=200, content={"message": "The pack has been modified"})


    # BORRAR UN PACK
    async def delete_pack(self, id: int, db: AsyncSession):
        async with db.begin():
            pack = (await db.execute(select(PackModel).filter(PackModel.id_pack == id))).scalars().first()
            if not pack:
                self.logger.warning('The pack to delete was not found')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no pack with that id")
        await db.execute(delete(PackModel).filter(PackModel.id_pack == id))
        await db.commit()
        self.logger.info('The pack has been removed')
        return JSONResponse(status_code=200, content={"message": "The pack has been removed"})