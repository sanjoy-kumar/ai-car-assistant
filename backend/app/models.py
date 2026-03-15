from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)


class Car(Base):

    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    mileage = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))

    maintenances = relationship("Maintenance", back_populates="car")


class Maintenance(Base):

    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True)
    service = Column(String)
    mileage = Column(Integer)

    car_id = Column(Integer, ForeignKey("cars.id"))

    car = relationship("Car", back_populates="maintenances")
