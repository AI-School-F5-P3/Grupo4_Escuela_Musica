from sqlalchemy import Float, Column, String, Integer
from config.db import Base


#Table Model
class LevelModel(Base):
    __tablename__ = "levels"
    id_level = Column(Integer, primary_key=True,  autoincrement=True)
    name_level = Column(String(100))

   

