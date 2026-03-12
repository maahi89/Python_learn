from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employee")
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)


@app.get("/employee")
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/employee/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    return crud.get_employee(db, emp_id)


@app.delete("/employee/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db, emp_id)
    return {"message": "Employee deleted"}