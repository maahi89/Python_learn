from sqlalchemy.orm import Session
from . import models


def create_employee(db: Session, emp):
    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


def delete_employee(db: Session, emp_id: int):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    db.delete(emp)
    db.commit()


def update_employee(db: Session, emp_id: int, emp):
    emp_db = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    for key, value in emp.dict().items():
        setattr(emp_db, key, value)
    db.commit()
    db.refresh(emp_db)
    return emp_db