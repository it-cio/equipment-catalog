from pydantic import BaseModel


class ConsumableBase(BaseModel):
    name: str
    price: int


class ConsumableCreate(ConsumableBase):
    pass


class Consumable(ConsumableBase):
    id: int
    compatibility: str

    class Config:
        orm_mode = True


class PartBase(BaseModel):
    name: str
    price: int


class PartCreate(PartBase):
    pass


class Part(PartBase):
    id: int
    compatibility: str
    consumables: list[Consumable] = []

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
