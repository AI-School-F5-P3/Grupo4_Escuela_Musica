from sqlalchemy import Float, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base


#Table Model
class Level_model(Base):
    __tablename__ = "niveles"
    id_level = Column(Integer, primary_key=True,  autoincrement=True)
    level = Column(String(100))

   

