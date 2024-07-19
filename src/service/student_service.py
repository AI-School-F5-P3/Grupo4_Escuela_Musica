from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from model.student_model import StudentModel
from scheme.student_scheme import Student
from config.db import get_async_session
from logger import Logs
from sqlalchemy.future import select
from sqlalchemy import delete


class Student_service:
    def __init__(self):
        #ya puedo acceder a la base de datos desde otros métodos
        self.logger= Logs()
        pass
       
    async def consult_student(self, db: AsyncSession):
        async with db.begin():
            result = (await db.execute(select(StudentModel))).scalars().all()
        self.logger.debug('Consult for all students')
        #obtain all StudentModel data y save in the variable result
        if not result:
            self.logger.warning("Didn't find Students")
        # If it doesn't find student, appear exception HTTP with state code 404 and error message
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"there is no any Student"}) 
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

    # Consult student by ID
    async def consult_student_id(self, db: AsyncSession, id: int):
        async with db.begin():
            result = (await db.execute(select(StudentModel).filter(StudentModel.id_student == id))).scalars().first()
        self.logger.debug(f'Consult student with id: {id}')
        # It get student data that I want to consult filtr by id
        # I get first I find and I keep in the variable result
        
        if not result:
            self.logger.warning('Student with the id did not exist')
            # Si no se encuentra el student, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message':'There is no Student with this id'})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

    # Add new student
    async def add_student(self, db: AsyncSession, data: Student):
        async with db.begin():
            student = (await db.execute(select(StudentModel).filter(StudentModel.id_student == data.id_student))).scalars().first()
            if student:
                self.logger.warning('Already exist a student with this id')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Already exist a student with this id")
            new_student = StudentModel(
                name_student=data.name_student,
                surname_student=data.surname_student,
                age_student=data.age_student,
                phone_student=data.phone_student,
                email_student=data.email_student,
                family_discount=data.family_discount
            )
            db.add(new_student)
            self.logger.info('Student has been added')
            await db.commit()
            return JSONResponse(status_code=201, content={"message": "A new student was registered", "id_student": new_student.id_student})



    # EDITAR UN student
    async def edit_student(self, db: AsyncSession, id: int, data: Student):
        async with db.begin():
            student = (await db.execute(select(StudentModel).filter(StudentModel.id_student == id))).scalars().first()
            if not student:
                self.logger.warning('There is no Student to edit')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no Student with this id")

            student.name_student = data.name_student
            student.surname_student = data.surname_student
            student.age_student = data.age_student
            student.email_student = data.email_student
            student.phone_student = data.phone_student
            student.family_discount = data.family_discount

            await db.commit()
            self.logger.info('Student has been modified')
            return JSONResponse(status_code=200, content={"message": "Student has been modified"})


    # Delete student
    async def delete_student(self, db: AsyncSession, id: int):
        async with db.begin():
            student = (await db.execute(select(StudentModel).filter(StudentModel.id_student == id))).scalars().first()
            if not student:
                self.logger.warning('There is no Student id to delete')
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no Student with this id")
            await db.execute(delete(StudentModel).filter(StudentModel.id_student == id))
            await db.commit()
            self.logger.info('Student has been deleted')
            return JSONResponse(status_code=200, content={"message": "Student has been deleted"})