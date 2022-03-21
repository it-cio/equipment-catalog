from sqlalchemy.orm import Session

from sql_app.models.equipments import EquipmentModel
from sql_app.models.parts import PartModel
from sql_app.models.consumables import ConsumableModel
from sql_app.schemas.equipments import EquipmentCreate
from sql_app.schemas.parts import PartCreate
from sql_app.schemas.consumables import ConsumableCreate


def get_equipment(db: Session, equipment_id: int):
    return db.query(EquipmentModel).filter(EquipmentModel.id == equipment_id).first()


def get_equipment_by_name(db: Session, name: str):
    return db.query(EquipmentModel).filter(EquipmentModel.name == name).first()


def get_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EquipmentModel).offset(skip).limit(limit).all()


def create_equipment(db: Session, equipment: EquipmentCreate):
    db_equipment = EquipmentModel(name=equipment.name)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


def get_parts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PartModel).offset(skip).limit(limit).all()


def create_equipment_part(db: Session, part: PartCreate, compatibility: str):
    db_part = PartModel(**part.dict(), compatibility=compatibility)
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part


def get_consumables(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ConsumableModel).offset(skip).limit(limit).all()


def create_part_consumable(db: Session, consumable: ConsumableCreate, compatibility: str):
    db_consumable = ConsumableModel(**consumable.dict(), compatibility=compatibility)
    db.add(db_consumable)
    db.commit()
    db.refresh(db_consumable)
    return db_consumable
