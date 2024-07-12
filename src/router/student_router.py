from fastapi import APIRouter, Depends
from scheme.student_scheme import Student
from service.student_service import Student_service
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_async_session


router = APIRouter( prefix="/student", tags=["student"])
student_service = Student_service()

# Create student table
# @alumnos.lifespan("startup")
# def startup():
#     # create db table
#     Base.metadata.create_all(bind=engine)


# Consult for every student
@router.get("/student/")
async def consult_student(db: AsyncSession = Depends(get_async_session)):
    return await student_service.consult_student(db)



# Consult student id
@router.get('/student/{id}')# id is the path parameter when the user access to this url
async def consult_student_id(id: int, db: AsyncSession = Depends(get_async_session)):
    return await student_service.consult_student_id(db, id)


# Add new student
@router.post("/student/")
async def add_student(Student: Student, db: AsyncSession = Depends(get_async_session)):
    return await student_service.add_student(db, Student)

# Edit
@router.put('/student/{id}')
async def edit_student(id: int, data: Student, db: AsyncSession = Depends(get_async_session)):
    return await student_service.edit_student(db, id, data)

# Delete student
@router.delete('/student/{id}')
async def delete_student(id: int, db: AsyncSession = Depends(get_async_session)):
    return await student_service.delete_student(db, id)

