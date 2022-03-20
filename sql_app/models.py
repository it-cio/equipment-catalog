from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class EquipmentModel(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    parts = relationship("PartModel", back_populates="equipments")


class PartModel(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)
    equipment_id = Column(Integer, ForeignKey("equipments.id"))

    equipments = relationship("EquipmentModel", back_populates="parts")
