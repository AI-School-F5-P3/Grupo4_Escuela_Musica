from sqlalchemy import Boolean, ForeignKey, Numeric, Table, Column, String, Float
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base


#Table model pack
class Packs_model(Base):
    __tablename__ = "pack"
    id_pack = Column(Integer, primary_key=True,  autoincrement=True)
    pack =Column(String(100))
    price_pack =Column(Float)
    first_discount =Column(Float)
    second_discount =Column(Float)

    
   