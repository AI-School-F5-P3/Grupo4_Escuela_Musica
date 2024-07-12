from sqlalchemy import Float, Column, String, Integer
from config.db import Base

#Table Model
class StudentModel(Base):
    __tablename__ = "student"
    id_student = Column(Integer, primary_key=True, autoincrement=True) 
    name_student = Column(String(100))
    surname_student = Column(String(100))
    age_student = Column(String(3))
    phone_student = Column(String(10))
    email_student = Column(String(30))
    family_discount = Column(Float, default=0.0)
    

