from fastapi.encoders import jsonable_encoder  # Import JSON encoder for FastAPI
from fastapi.responses import JSONResponse  # Import JSONResponse for sending JSON responses
from model.level_model import LevelModel  # Import the TeacherModel from the model module
from scheme.level_scheme import Level # Import the Teacher schema
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from sqlalchemy import and_
from fastapi import HTTPException, status  # Import HTTPException and status codes from FastAPI
from sqlalchemy.future import select  # Import select for constructing SQL queries
from sqlalchemy import delete  # Import delete for constructing delete queries
from logger import Logs  # Import the logging setup

class LevelService:
    def __init__(self):
        self.logger = Logs()  # Initialize the logger

    # Consult for every teacher
    async def consult_levels(self, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            result = (await db.execute(select(LevelModel))).scalars().all()  # Execute a query to select all levels
        self.logger.debug('Consult for every level')  # Log the action
        if not result:  # If no level are found
            self.logger.warning('Level not found')  # Log a warning
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no Levels yet")  # Raise a 404 error
        return JSONResponse(status_code=200, content=jsonable_encoder(result))  # Return the result as a JSON response

    # Consult a Level 
    async def consult_level(self, db: AsyncSession, name: str):
        async with db.begin():  # Begin a database transaction
            result = (await db.execute(select(LevelModel).filter(LevelModel.name_level == name))).scalars().first()
        self.logger.debug(f'Querying level by name')
        if not result:
            self.logger.warning('Level not found')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no level with that name")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))



    # Add a teacher
    async def add_level(self, data: Level, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            new_level = LevelModel(
                name_level=data.name_level,           
            )
                  # Create a new level instance
            db.add(new_level)  # Add the new level to the database session
            await db.commit()  # Commit the transaction
            self.logger.info("A new teacher has registered")  # Log the action
            return JSONResponse(status_code=201, content={"message": "A new level has registered"})  # Return a success message



    # Edit a level
    async def edit_level(self, id: int, data: Level, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            level = (await db.execute(select(LevelModel).filter(LevelModel.id_level == id,))).scalars().first()  # Find the level by name
            if not level:  # If no level is found
                self.logger.warning('Level not found to edit')  # Log a warning
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message':'There is no level to edit'})  # Raise a 404 error
            # Update the level's details
            level.name_level = data.name_level
            await db.commit()  # Commit the transaction
            self.logger.info('The level has been changed')  # Log the action
            return JSONResponse(status_code=200, content={"message": "The level has been changed"})  # Return a success message

    # Delete a level
    async def delete_level(self, id: int, db: AsyncSession):
        async with db.begin():  # Begin a database transaction
            level = (await db.execute(select(LevelModel).filter(LevelModel.id_level == id))).scalars().first()  # Find the level by name
            if not level:  # If no teacher is found
                self.logger.warning('Level not found to delete')  # Log a warning
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no level to delete")  # Raise a 404 error
            await db.execute(delete(LevelModel).filter(LevelModel.id_level == id))  # Execute the delete query
            await db.commit()  # Commit the transaction
            self.logger.info('The level has been removed')  # Log the action
            return JSONResponse(status_code=200, content={"message": "The level has been removed"})  # Return a success message
