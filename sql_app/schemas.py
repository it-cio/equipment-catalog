from pydantic import BaseModel


class PartBase(BaseModel):
    name: str
    price: int


class PartCreate(PartBase):
    pass


class Part(PartBase):
    id: int
    compatibility: str

    class Config:
        orm_mode = True


class EquipmentBase(BaseModel):
    name: str


class EquipmentCreate(EquipmentBase):
    pass


class Equipment(EquipmentBase):
    id: int
    parts: list[Part] = []

    class Config:
        orm_mode = True
