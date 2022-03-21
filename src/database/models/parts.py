from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database.sql import Base


class PartModel(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)

    compatibility = Column(String, ForeignKey("equipments.name"))
    equipments = relationship("EquipmentModel", back_populates="parts")
    consumables = relationship("ConsumableModel", back_populates="parts")
