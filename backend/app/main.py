from fastapi import FastAPI

from .database import Base, engine
from .routers import cars, maintenance, ai
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(cars.router)
app.include_router(maintenance.router)
app.include_router(ai.router)
