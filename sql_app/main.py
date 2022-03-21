from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud
from .database import SessionLocal, engine
from sql_app.database import Base
from sql_app.schemas.equipments import EquipmentCreate, Equipment
from sql_app.schemas.parts import PartCreate, Part
from sql_app.schemas.consumables import ConsumableCreate


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/equipments/", response_model=Equipment)
def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = crud.get_equipment_by_name(db, name=equipment.name)
    if db_equipment:
        raise HTTPException(status_code=400, detail=f"{equipment.name} already exist")
    return crud.create_equipment(db=db, equipment=equipment)


@app.get("/equipments/", response_model=list[Equipment])
def get_all_equipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipments = crud.get_equipments(db, skip=skip, limit=limit)
    return equipments


@app.get("/equipments/{equipment_id}", response_model=Equipment)
def get_one_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = crud.get_equipment(db, equipment_id=equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment


@app.get("/parts/", response_model=list[Equipment])
def get_all_parts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    parts = crud.get_parts(db, skip=skip, limit=limit)
    return parts


@app.post("/equipments/{compatibility}/parts/", response_model=Equipment)
def create_part_for_equipment(
    compatibility: str, part: PartCreate, db: Session = Depends(get_db)
):
    compatibility = ", ".join(compatibility.replace(',', ' ').strip().lower().title().split())
    return crud.create_equipment_part(db=db, part=part, compatibility=compatibility)


@app.get("/consumables/", response_model=list[Part])
def get_all_consumables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    consumables = crud.get_consumables(db, skip=skip, limit=limit)
    return consumables


@app.post("/parts/{compatibility}/consumables/", response_model=Part)
def create_consumable_for_part(
    compatibility: str, consumable: ConsumableCreate, db: Session = Depends(get_db)
):
    compatibility = ", ".join(compatibility.replace(',', ' ').strip().lower().title().split())
    return crud.create_part_consumable(db=db, consumable=consumable, compatibility=compatibility)
