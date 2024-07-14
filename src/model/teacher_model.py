from sqlalchemy import Table, Column, String, Integer   # Import Integer type from SQLAlchemy
from config.db import meta, engine, Base  # Import metadata, engine, and Base class from config.db

# Define the Teacher_model class, inheriting from Base which represents the SQLAlchemy base class
class TeacherModel(Base):
    __tablename__ = "teacher"  # Table name in the database

    # Columns definition for the 'teacher' table
    id_teacher = Column(Integer, primary_key=True, autoincrement=True)  # Integer primary key with auto-increment
    name_teacher = Column(String(100))  # String column for teacher's name (max length 100)
    surname_teacher = Column(String(100))  # String column for teacher's surname (max length 100)
    email_teacher = Column(String(50))  # String column for teacher's email (max length 50)

