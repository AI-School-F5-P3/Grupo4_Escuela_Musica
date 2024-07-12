from sqlalchemy import ForeignKey, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine, Base

# Teacher table model
class teacher_class_model(Base):
    __tablename__ = "teacher_class"
    id_class_teacher = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey("class.id_class"))
    teacher_id = Column(Integer, ForeignKey ("teacher.id_teacher"))
    level_id = Column(Integer, ForeignKey("level.id_level"))
