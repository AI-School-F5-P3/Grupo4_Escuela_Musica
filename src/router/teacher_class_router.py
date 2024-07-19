from fastapi import APIRouter, Depends  # Import APIRouter and Depends from FastAPI for routing and dependency injection
from scheme.teacher_class_scheme import TeacherClass  # Import the Class schema
from service.teacher_class_service import TeacherClassService  # Import the ClassService class
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from config.db import get_async_session  # Import the function to get an async session

# Create an APIRouter instance with a prefix and tags for routes related to classes
router = APIRouter(prefix="/teacher_class", tags=["teacher_classes"])
# Instantiate the ClassService class
teacher_class_service = TeacherClassService()

# Consult all classes
@router.get('/')
# Define an async function to consult all classes, with dependency injection for the database session
async def consult_classes_teacher(db: AsyncSession = Depends(get_async_session)):
    return await teacher_class_service.consult_teacher_classes(db)  # Call the consult_classes method from class_service

# Consult a class by id
@router.get('/{id}')  # 'id' is the path parameter when the user accesses this URL
# Define an async function to consult a class by id, with dependency injection for the database session
async def consult_teache_class_id(id: int, db: AsyncSession = Depends(get_async_session)):
    return await teacher_class_service.consult_teacher_class_id(id, db)  # Call the consult_class_id method from class_service

# Add a new class
@router.post('/')
# Define an async function to add a new class, with dependency injection for the database session
async def add_class_teacher(data: TeacherClass, db: AsyncSession = Depends(get_async_session)):
    return await teacher_class_service.add_teacher_class(data, db)  # Call the add_class method from class_service

# Edit a class's details
@router.put('/{id}')
# Define an async function to edit a class's details, with dependency injection for the database session
async def edit_class_teacher(id: int, data: TeacherClass, db: AsyncSession = Depends(get_async_session)):
    return await teacher_class_service.edit_teacher_class(id, data, db)  # Call the edit_class method from class_service

# Delete a class
@router.delete('/{id}')
# Define an async function to delete a class, with dependency injection for the database session
async def delete_class_teacher(id: int, db: AsyncSession = Depends(get_async_session)):
    return await teacher_class_service.delete_teacher_class(id, db)  # Call the delete_class method from class_service
