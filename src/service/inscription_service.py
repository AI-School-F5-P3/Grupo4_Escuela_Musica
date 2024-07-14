from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from model.student_model import StudentModel
from model.inscription_model import InscriptionModel
from scheme.inscription_scheme import Inscription
from dateutil.relativedelta import relativedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, text
from service.teacher_class_service import TeacherClassService
from logger import Logs
from sqlalchemy.future import select
from sqlalchemy import delete


class InscriptionService:
    def __init__(self):
        self.logger = Logs()
    

    async def consult_inscriptions(self, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(InscriptionModel))).scalars().all()
        self.logger.debug('Consult all inscriptions')
        if not result:
            self.logger.warning("Inscriptions not found")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No insctiptions exists")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    

    async def consult_inscription_id(self, id:int, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(InscriptionModel.filter(InscriptionModel.id_inscription == id)))).scalars().all()
        self.logger.debug('Consult inscription by id: {id}')
        if not result:
            self.logger.warning("Inscription with the id - {id}  not found")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Inscription with the id - {id}  not found")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    



