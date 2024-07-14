from sqlalchemy import ForeignKey, Table, Column, String, Integer
from config.db import meta, engine, Base

# Teacher table model
class ClassModel(Base): 
    __tablename__ = "class"
    id_class =Column(Integer, primary_key=True, autoincrement=True)
    name_class =Column(String(50))
    id_pack =Column(Integer, ForeignKey("pack.id_pack"))
