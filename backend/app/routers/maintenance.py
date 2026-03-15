from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Maintenance
from ..schemas import MaintenanceCreate

router = APIRouter()


@router.post("/maintenance")
def add_maintenance(data: MaintenanceCreate, db: Session = Depends(get_db)):

    record = Maintenance(**data.dict())

    db.add(record)
    db.commit()

    return {"message": "Maintenance added"}
