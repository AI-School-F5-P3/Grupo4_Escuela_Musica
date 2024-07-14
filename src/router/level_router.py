from fastapi import APIRouter, Depends  # Import APIRouter and Depends from FastAPI for routing and dependency injection
from scheme.level_scheme import Level  # Import the Level schema
from service.level_service import LevelService  # Import the LevelService class
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from config.db import get_async_session  # Import the function to get an async session

# Create an APIRouter instance with a prefix and tags for routes related to levels
router = APIRouter(prefix="/level", tags=["level"])
# Instantiate the LevelService class
level_service = LevelService()

# Consult all levels
@router.get('/')
# Define an async function to consult all levels, with dependency injection for the database session
async def consult_levels(db: AsyncSession = Depends(get_async_session)):
    return await level_service.consult_levels(db)  # Call the consult_levels method from level_service

# Consult a level by id
@router.get('/{name}')  # 'id' is the path parameter when the user accesses this URL
# Define an async function to consult a level by id, with dependency injection for the database session
async def consult_level(name: str, db: AsyncSession = Depends(get_async_session)):
    return await level_service.consult_level(db, name)  # Call the consult_level method from level_service

# Add a new level
@router.post('/')
# Define an async function to add a new level, with dependency injection for the database session
async def add_level(data: Level, db: AsyncSession = Depends(get_async_session)):
    return await level_service.add_level(data, db)  # Call the add_level method from level_service

# Edit a level's details
@router.put('/{id}')
# Define an async function to edit a level's details, with dependency injection for the database session
async def edit_level(id: int, data: Level, db: AsyncSession = Depends(get_async_session)):
    return await level_service.edit_level(id, data, db)  # Call the edit_level method from level_service

# Delete a level
@router.delete('/{id}')
# Define an async function to delete a level, with dependency injection for the database session
async def delete_level(id: int, db: AsyncSession = Depends(get_async_session)):
    return await level_service.delete_level(id, db)  # Call the delete_level method from level_service
