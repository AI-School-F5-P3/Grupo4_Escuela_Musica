from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import text
from model.teacher_class_model import TeacherClassModel
from scheme.teacher_class_scheme import TeacherClass
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from fastapi import HTTPException, status
from logger import Logs

class TeacherClassService:
    def __init__(self) :
        self.logger= Logs()


    # CONSULTAR TODAS LAS RELACIONES 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    async def consult_teacher_classes(self, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(TeacherClassModel))).scalars().all()
        self.logger.debug('Consulting all teachers by class')
        if not result:
            self.logger.warning('No teachers found for classes')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= ('There are no "teacher - class - level" relationships yet'))
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    async def consult_teacher_class_id(self, id: int, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(TeacherClassModel).filter(TeacherClassModel.id_class_teacher == id))).scalars().first()
        self.logger.debug(f'Consulting teacher by classes and level by id')
        if not result:
            self.logger.warning('The teacher was not found by class and level')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no 'teacher - class - level' relationship with that id")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    async def consult_class_teacher_level_by_class_name(self, name: str, db: AsyncSession):
        query = f"""SELECT teacher_class.id_class_teacher, class.name_class, level.name_level, teacher.name_teacher
                            FROM teacher_class
                            JOIN class
                            ON class.id_class = teacher_class.id_class
                            JOIN level
                            ON level.id_level = teacher_class.id_level
                            JOIN teacher
                            ON teacher.id_teacher = teacher_class.id_teacher
                            WHERE class.name_class = :name"""

        async with db.begin():
            result = (await db.execute(text(query), {'name': name}))
            rows = result.all()

        result_dicts = [{'id': row[0], 'class name': row[1], 'level': row[2], 'teacher': row[3]} for row in rows]
        if not rows:
            self.logger.warning('The teacher was not found by class and level')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Relationship 'teacher - class -level' not found")
        return JSONResponse(status_code=200, content=jsonable_encoder(result_dicts))

    # CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    async def consult_teacher_class_level_by_teacher_name(self, name: str, db: AsyncSession):
        query = f"""SELECT teacher.name_teacher, class.name_class, level.name_level, teacher_class.id_class_teacher
                    FROM teacher_class
                    JOIN class
                    ON class.id_class = teacher_class.id_class
                    JOIN level
                    ON level.id_level = teacher_class.id_level
                    JOIN teacher
                    ON teacher.id_teacher = teacher_class.id_teacher
                    WHERE teacher.name_teacher = :name"""

        async with db.begin():
            result = await db.execute(text(query), {"name": name})
            rows = result.all()

        result_dicts = [{'teacher': row[0], 'class name': row[1], 'level': row[2], 'id_class_teacher': row[3]} for row in rows]
        if not result:
            self.logger.warning('The teacher was not found by class and level')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Relationship 'teacher - class -level' not found")
        return JSONResponse(status_code=200, content=jsonable_encoder(result_dicts))


    # AGREGAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL'
    async def add_teacher_class(self, data: TeacherClass, db: AsyncSession):
        async with db.begin():
            teacher_class = (await db.execute(select(TeacherClassModel).filter(TeacherClassModel.id_class_teacher == data.id_class_teacher))).scalars().first()
            if teacher_class:
                self.logger.warning('The teacher by class and level already exists with this id')
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="There is already a relationship 'teacher - class - level' with this id")
            new_teacher_class = TeacherClassModel(
                id_class = data.id_class,
                id_teacher = data.id_teacher,
                id_level = data.id_level
                )
                
            db.add(new_teacher_class)
            await db.commit()
            self.logger.info("A new teacher has been registered for classes and level")
            return JSONResponse(status_code=201, content={"message": "A new relationship 'teacher - class - level' has been registered"})


    # EDITAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL'
    async def edit_teacher_class(self, id: int, data: TeacherClass, db: AsyncSession):
        async with db.begin():
            teacher_class = (await db.execute(select(TeacherClassModel).filter(TeacherClassModel.id_class_teacher == id))).scalars().first()
            if not teacher_class:
                self.logger.warning('The teacher by class and level was not found to edit')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no relationship 'teacher - class - level' with that id")

            teacher_class.id_class = data.id_class
            teacher_class.id_teacher = data.id_teacher
            teacher_class.id_level = data.id_level

            await db.commit()
            self.logger.info('The teacher has been modified by class and level')
            return JSONResponse(status_code=200, content={"message": "Relationship 'teacher - class - level' updated correctly"})


    # BORRAR UNA RELACIÓN RELACIÓN 'PROFESOR - CLASE - NIVEL'
    async def delete_teacher_class(self, id: int, db: AsyncSession):
        async with db.begin():
          teacher_class = (await db.execute(select(TeacherClassModel).filter(TeacherClassModel.id_class_teacher == id))).scalars().first()
          if not teacher_class:
            self.logger.warning('The teacher was not found by class and level to delete')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no relationship 'teacher - class - level' with that id")
          await db.execute(delete(TeacherClassModel).filter(TeacherClassModel.id_class_teacher == id))
          await db.commit()
          self.logger.info('The teacher has been removed by class and level')
          return JSONResponse(status_code=200, content={"message": "The 'teacher - class - level' relationship has been removed"})
