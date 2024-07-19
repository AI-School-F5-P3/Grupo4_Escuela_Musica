from sqlalchemy import Boolean, ForeignKey, Numeric, Table, Column, String, Float, Integer  # Import necessary SQLAlchemy components
from config.db import Base  # Import the Base class for declarative class definitions

# Table model for pack
class PackModel(Base):
    __tablename__ = "pack"  # Define the table name in the database
    id_pack = Column(Integer, primary_key=True, autoincrement=True)  # Primary key column, auto-incremented
    name_pack = Column(String(100))  # Column for the name of the pack, up to 100 characters
    price_pack = Column(Float)  # Column for the price of the pack, stored as a float
    first_discount = Column(Float)  # Column for the first discount on the pack, stored as a float
    second_discount = Column(Float)  # Column for the second discount on the pack, stored as a float

   