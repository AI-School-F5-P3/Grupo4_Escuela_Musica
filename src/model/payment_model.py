from sqlalchemy import Float, Column, ForeignKey, String, DateTime, Integer
from config.db import Base

class PaymentModel(Base):
    __tablename__ = "payment"
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    inscripcion_id = Column(Integer, ForeignKey("inscription.id_inscription"))
    payment_day = Column(String(20))