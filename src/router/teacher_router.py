from fastapi import APIRouter, Depends  # Import APIRouter and Depends from FastAPI for routing and dependency injection
from scheme.teacher_scheme import Teacher  # Import the Teacher schema
from service.teacher_service import TeacherService  # Import the TeacherService class
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from config.db import get_async_session  # Import the function to get an async session

# Create an APIRouter instance with a prefix and tags for routes related to teachers
router = APIRouter(prefix="/teacher", tags=["teacher"])
# Instantiate the TeacherService class
teacher_service = TeacherService()

# Create tables (commented out, as it is usually handled in a different part of the application)
# @router.on_event("startup")
# def startup():
#     Base.metadata.create_all(bind=engine)

# Consult all teachers
@router.get('')
# Define an async function to consult all teachers, with dependency injection for the database session
async def consult_teacher(db: AsyncSession = Depends(get_async_session)):
    return await teacher_service.consult_teachers(db)  # Call the consult_teacher method from teacher_service

# Consult a teacher by name
@router.get('/{name},{surname}')  # 'name' is the path parameter received when the user accesses this URL
# Define an async function to consult a teacher by name, with dependency injection for the database session
async def consult_teacher_name(name: str, surname: str, db: AsyncSession = Depends(get_async_session)):
    return await teacher_service.consult_teacher(db, name, surname)  # Call the consult_teacher method from teacher_service with name

# Add a new teacher
@router.post('')
# Define an async function to add a new teacher, with dependency injection for the database session
async def add_teacher(data: Teacher, db: AsyncSession = Depends(get_async_session)):
    return await teacher_service.add_teacher(data, db)  # Call the add_profesor method from teacher_service

# Edit a teacher's details
@router.put('/{id}')
# Define an async function to edit a teacher's details, with dependency injection for the database session
async def edit_teacher(id: int, data: Teacher, db: AsyncSession = Depends(get_async_session)):
    return await teacher_service.edit_teacher(id, data, db)  # Call the edit_teacher method from teacher_service

# Delete a teacher
@router.delete('/{id}')
# Define an async function to delete a teacher, with dependency injection for the database session
async def delete_teacher(id: int, db: AsyncSession = Depends(get_async_session)):
    return await teacher_service.delete_teacher(id, db)  # Call the delete_teacher method from teacher_service

