from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql_app.database import Base


class EquipmentModel(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    parts = relationship("PartModel", back_populates="equipments")