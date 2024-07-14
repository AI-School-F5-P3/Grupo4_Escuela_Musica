from fastapi import APIRouter, Depends  # Import APIRouter and Depends from FastAPI for routing and dependency injection
from scheme.class_scheme import Class  # Import the Class schema
from service.class_service import ClassService  # Import the ClassService class
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from config.db import get_async_session  # Import the function to get an async session

# Create an APIRouter instance with a prefix and tags for routes related to classes
router = APIRouter(prefix="/class", tags=["classes"])
# Instantiate the ClassService class
class_service = ClassService()

# Consult all classes
@router.get('/')
# Define an async function to consult all classes, with dependency injection for the database session
async def consult_classes(db: AsyncSession = Depends(get_async_session)):
    return await class_service.consult_classes(db)  # Call the consult_classes method from class_service

# Consult a class by id
@router.get('/{id}')  # 'id' is the path parameter when the user accesses this URL
# Define an async function to consult a class by id, with dependency injection for the database session
async def consult_class_id(id: int, db: AsyncSession = Depends(get_async_session)):
    return await class_service.consult_class_id(id, db)  # Call the consult_class_id method from class_service

# Add a new class
@router.post('/')
# Define an async function to add a new class, with dependency injection for the database session
async def add_class(data: Class, db: AsyncSession = Depends(get_async_session)):
    return await class_service.add_class(data, db)  # Call the add_class method from class_service

# Edit a class's details
@router.put('/{id}')
# Define an async function to edit a class's details, with dependency injection for the database session
async def edit_class(id: int, data: Class, db: AsyncSession = Depends(get_async_session)):
    return await class_service.edit_class(id, data, db)  # Call the edit_class method from class_service

# Delete a class
@router.delete('/{id}')
# Define an async function to delete a class, with dependency injection for the database session
async def delete_class(id: int, db: AsyncSession = Depends(get_async_session)):
    return await class_service.delete_class(id, db)  # Call the delete_class method from class_service

