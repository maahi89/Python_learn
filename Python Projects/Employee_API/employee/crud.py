from sqlalchemy.orm import Session
import models
import schemas

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