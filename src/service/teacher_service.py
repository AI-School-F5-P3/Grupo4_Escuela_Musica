from fastapi.encoders import jsonable_encoder  # Import JSON encoder for FastAPI
from fastapi.responses import JSONResponse  # Import JSONResponse for sending JSON responses
from model.teacher_model import TeacherModel  # Import the TeacherModel from the model module
from scheme.teacher_scheme import Teacher  # Import the Teacher schema
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from sqlalchemy import and_
from fastapi import HTTPException, status  # Import HTTPException and status codes from FastAPI
from sqlalchemy.future import select  # Import select for constructing SQL queries
from sqlalchemy import delete  # Import delete for constructing delete queries
from logger import Logs  # Import the logging setup

class TeacherService:
    def __init__(self):
        self.logger = Logs()  # Initialize the logger

    # Consult for every teacher
    async def consult_teachers(self, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            result = (await db.execute(select(TeacherModel))).scalars().all()  # Execute a query to select all teachers
        self.logger.debug('Consult for every teacher')  # Log the action
        if not result:  # If no teachers are found
            self.logger.warning('Teacher not found')  # Log a warning
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no teachers yet")  # Raise a 404 error
        return JSONResponse(status_code=200, content=jsonable_encoder(result))  # Return the result as a JSON response

    # Consult a teacher by name
    async def consult_teacher(self, db: AsyncSession, name: str, surname: str):
        async with db.begin():  # Begin a database transaction
            result = (await db.execute(select(TeacherModel).filter(and_(TeacherModel.name_teacher == name, TeacherModel.surname_teacher == surname)))).scalars().first()  # Execute a query to select a teacher by name
        self.logger.debug('Consult teacher by name')  # Log the action
        if not result:  # If no teacher is found
            self.logger.warning('Teacher not found')  # Log a warning
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")  # Raise a 404 error
        return JSONResponse(status_code=200, content=jsonable_encoder(result))  # Return the result as a JSON response



    # Add a teacher
    async def add_teacher(self, data: Teacher, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            new_teacher = TeacherModel(
                name_teacher=data.name_teacher,
                surname_teacher=data.surname_teacher,
                email_teacher=data.email_teacher           
            )
                  # Create a new teacher instance
            db.add(new_teacher)  # Add the new teacher to the database session
            await db.commit()  # Commit the transaction
            self.logger.info("A new teacher has registered")  # Log the action
            return JSONResponse(status_code=201, content={"message": "A new teacher has registered"})  # Return a success message



    # Edit a teacher
    async def edit_teacher(self, id: int, data: Teacher, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            teacher = (await db.execute(select(TeacherModel).filter(TeacherModel.id_teacher == id,))).scalars().first()  # Find the teacher by name
            if not teacher:  # If no teacher is found
                self.logger.warning('Teacher not found to edit')  # Log a warning
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message':'There is no teacher with that id'})  # Raise a 404 error
            # Update the teacher's details
            teacher.name_teacher = data.name_teacher
            teacher.surname_teacher = data.surname_teacher
            teacher.email_teacher = data.email_teacher
            await db.commit()  # Commit the transaction
            self.logger.info('The teacher has been changed')  # Log the action
            return JSONResponse(status_code=200, content={"message": "The teacher has been changed"})  # Return a success message

    # Delete a teacher
    async def delete_teacher(self, id: int, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            teacher = (await db.execute(select(TeacherModel).filter(TeacherModel.id_teacher == id))).scalars().first()  # Find the teacher by name
            if not teacher:  # If no teacher is found
                self.logger.warning('Teacher not found to delete')  # Log a warning
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no teacher with that id")  # Raise a 404 error
            await db.execute(delete(TeacherModel).filter(TeacherModel.id_teacher == id))  # Execute the delete query
            await db.commit()  # Commit the transaction
            self.logger.info('The teacher has been removed')  # Log the action
            return JSONResponse(status_code=200, content={"message": "The teacher has been removed"})  # Return a success message
