import re
from pydantic import BaseModel, validator
from src.schemas.parts import Part


class EquipmentBase(BaseModel):
    name: str


class EquipmentCreate(EquipmentBase):
    @validator('name')
    def name_match(cls, name):
        if re.match(r'^[а-яА-Я.,!@#$%^&/+=]+$', name):
            raise ValueError(f"Name '{name}' is incorrect")
        return name.lower().title()


class Equipment(EquipmentBase):
    id: int
    parts: list[Part] = []

    class Config:
        orm_mode = True
