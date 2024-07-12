from sqlalchemy import Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine, Base


# Teacher table
class Teacher_model(Base):
    __tablename__ = "teacher"
    id_teacher = Column(Integer, primary_key=True, autoincrement=True)
    name_teacher = Column(String(100))
    surname_teacher = Column(String(100))
    email_teacher = Column(String(50))

