from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Car
from ..schemas import CarCreate

router = APIRouter()


@router.post("/add_car")
def add_car(car: CarCreate, db: Session = Depends(get_db)):

    new_car = Car(**car.dict())

    db.add(new_car)
    db.commit()

    return {"message": "Car added"}
