from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql_app.database import Base


class ConsumableModel(Base):
    __tablename__ = "consumables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)

    compatibility = Column(String, ForeignKey("parts.name"))
    parts = relationship("PartModel", back_populates="consumables")