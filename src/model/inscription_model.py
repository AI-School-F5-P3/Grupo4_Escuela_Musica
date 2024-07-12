from sqlalchemy import Boolean, Date, Float, ForeignKey, Column,String, Integer,func
from config.db import Base

#Table Inscriptions Model
class Inscription_model(Base):
    __tablename__ = "inscription"
    id_inscripcion = Column(Integer, primary_key=True, autoincrement=True)
    teacher_class_id = Column(Integer, ForeignKey("teacher_class.id_class_teacher"))
    student_id = Column(Integer, ForeignKey("student.id_student"))
    price_class = Column(String(20))
    discount_inscription = Column(Float)
    family_discount = Column(Float)
    discount_price = Column(String(10))
    paid = Column(String(10))
    inscription_date = Column(Date)
    finish_date = Column(Date)
  
