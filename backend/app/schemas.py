from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    mileage: int


class MaintenanceCreate(BaseModel):
    service: str
    mileage: int
    car_id: int


class AskAI(BaseModel):
    question: str
    make: str
    model: str
    year: int
    mileage: int
