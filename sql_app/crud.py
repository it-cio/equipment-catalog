from sqlalchemy.orm import Session

from . import models, schemas


def get_equipment(db: Session, equipment_id: int):
    return db.query(models.EquipmentModel).filter(models.EquipmentModel.id == equipment_id).first()


def get_equipment_by_name(db: Session, name: str):
    return db.query(models.EquipmentModel).filter(models.EquipmentModel.name == name).first()


def get_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EquipmentModel).offset(skip).limit(limit).all()


def create_equipment(db: Session, equipment: schemas.EquipmentCreate):
    db_equipment = models.EquipmentModel(name=equipment.name)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


def get_parts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PartModel).offset(skip).limit(limit).all()


def create_equipment_part(db: Session, part: schemas.PartCreate, equipment_id: int):
    db_part = models.PartModel(**part.dict(), equipment_id=equipment_id)
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part
