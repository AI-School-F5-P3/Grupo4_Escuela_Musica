from sqlalchemy import Boolean, Date, Float, ForeignKey, Column,String, Integer,func
from config.db import Base

#Table Inscriptions Model
class InscriptionModel(Base):
   __tablename__ = "inscription"
   id_inscription = Column(Integer, primary_key=True, autoincrement=True)
   id_class_teacher = Column(Integer, ForeignKey("teacher_class.id_class_teacher"))
   id_student = Column(Integer, ForeignKey("student.id_student"))
   price_class = Column(Float)
   discount_inscription = Column(Float)
   family_discount = Column(Float)
   price_with_discount = Column(Float)
   paid = Column(Boolean)
   inscription_date = Column(Date)
   end_date = Column(Date)
   
