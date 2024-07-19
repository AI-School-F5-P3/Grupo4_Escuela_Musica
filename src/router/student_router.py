from fastapi import APIRouter, Depends  # Import FastAPI APIRouter and Depends for dependency injection
from scheme.student_scheme import Student  # Import the Student schema
from service.student_service import Student_service  # Import the Student_service class
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for asynchronous database operations
from config.db import get_async_session  # Import the function to get an async session

# Create a new APIRouter instance with a prefix and tags
router = APIRouter(prefix="/student", tags=["student"])
# Instantiate the Student_service class
student_service = Student_service()

# Consult for every student
@router.get("")
# Define an async function to consult all students, with dependency injection for the database session
async def consult_student(db: AsyncSession = Depends(get_async_session)):
    return await student_service.consult_student(db)  # Call the consult_student method from student_service

# Consult student by id
@router.get('/{id}')  # id is the path parameter when the user accesses this URL
# Define an async function to consult a student by id, with dependency injection for the database session
async def consult_student_id(id: int, db: AsyncSession = Depends(get_async_session)):
    return await student_service.consult_student_id(db, id)  # Call the consult_student_id method from student_service

# Add new student
@router.post("")
# Define an async function to add a new student, with dependency injection for the database session
async def add_student(data: Student, db: AsyncSession = Depends(get_async_session)):
    return await student_service.add_student(db, data)  # Call the add_student method from student_service

# Edit student
@router.put('/{id}')
# Define an async function to edit a student, with dependency injection for the database session
async def edit_student(id: int, data: Student, db: AsyncSession = Depends(get_async_session)):
    return await student_service.edit_student(db, id, data)  # Call the edit_student method from student_service

# Delete student
@router.delete('/{id}')
# Define an async function to delete a student, with dependency injection for the database session
async def delete_student(id: int, db: AsyncSession = Depends(get_async_session)):
    return await student_service.delete_student(db, id)  # Call the delete_student method from student_service

