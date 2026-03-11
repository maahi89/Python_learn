from fastapi import FastAPI
from .database import engine, Base
from .routers import students

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(students.router)
