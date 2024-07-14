from sqlalchemy import Table, Column, String, Integer, ForeignKey
from config.db import meta, engine, Base

# Table teacher models
class TeacherClassModel(Base):
    __tablename__ = "teacher_class"
    id_class_teacher = Column(Integer, primary_key=True, autoincrement=True)
    id_class = Column(Integer, ForeignKey("class.id_class"))
    id_teacher = Column(Integer, ForeignKey ("teacher.id_teacher"))
    id_level = Column(Integer, ForeignKey("levels.id_level"))
