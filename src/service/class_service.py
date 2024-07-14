from fastapi.encoders import jsonable_encoder  # Import JSON encoder for FastAPI
from fastapi.responses import JSONResponse  # Import JSONResponse for sending JSON responses
from model.class_model import ClassModel  # Import the ClassModel from the model module
from scheme.class_scheme import Class  # Import the Class schema
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from sqlalchemy import and_
from fastapi import HTTPException, status  # Import HTTPException and status codes from FastAPI
from sqlalchemy.future import select  # Import select for constructing SQL queries
from sqlalchemy import delete  # Import delete for constructing delete queries
from logger import Logs  # Import the logging setup

class ClassService:
    def __init__(self):
        self.logger = Logs()  # Initialize the logger

    # Consult for every class
    async def consult_classes(self, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            result = (await db.execute(select(ClassModel))).scalars().all()  # Execute a query to select all classes
        self.logger.debug('Consult for every class')  # Log the action
        if not result:  # If no classes are found
            self.logger.warning('Class not found')  # Log a warning
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no classes yet")  # Raise a 404 error
        return JSONResponse(status_code=200, content=jsonable_encoder(result))  # Return the result as a JSON response

    # Consult a class by name
    async def consult_class_id(self, id: int, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            result = (await db.execute(select(ClassModel).filter(and_(ClassModel.id_class == id)))).scalars().first()  # Execute a query to select a class by id
        self.logger.debug('Consult class by id')  # Log the action
        if not result:  # If no class is found
            self.logger.warning('Class not found')  # Log a warning
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")  # Raise a 404 error
        return JSONResponse(status_code=200, content=jsonable_encoder(result))  # Return the result as a JSON response

    # Add a class
    async def add_class(self, data: Class, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            new_class = ClassModel(
                name_class=data.name_class,
                id_pack=data.id_pack

            )  # Create a new class instance
            db.add(new_class)  # Add the new class to the database session
            await db.commit()  # Commit the transaction
            self.logger.info("A new class has been registered")  # Log the action
            return JSONResponse(status_code=201, content={"message": "A new class has been registered"})  # Return a success message

    # Edit a class
    async def edit_class(self, id: int, data: Class, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            class_ = (await db.execute(select(ClassModel).filter(ClassModel.id_class == id))).scalars().first()  # Find the class by ID
            if not class_:  # If no class is found
                self.logger.warning('Class not found to edit')  # Log a warning
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no class with that id")  # Raise a 404 error
            # Update the class's details
            class_.name_class = data.name_class
            class_.id_pack = data.id_pack
         
            await db.commit()  # Commit the transaction
            self.logger.info('The class has been changed')  # Log the action
            return JSONResponse(status_code=200, content={"message": "The class has been changed"})  # Return a success message

    # Delete a class
    async def delete_class(self, id: int, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            class_ = (await db.execute(select(ClassModel).filter(ClassModel.id_class == id))).scalars().first()  # Find the class by ID
            if not class_:  # If no class is found
                self.logger.warning('Class not found to delete')  # Log a warning
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no class with that id")  # Raise a 404 error
            await db.execute(delete(ClassModel).filter(ClassModel.id_class == id))  # Execute the delete query
            await db.commit()  # Commit the transaction
            self.logger.info('The class has been removed')  # Log the action
            return JSONResponse(status_code=200, content={"message": "The class has been removed"})  # Return a success message
