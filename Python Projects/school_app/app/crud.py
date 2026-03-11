from sqlalchemy.orm import Session
from . import models, schemas

# CREATE
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# READ ALL
def get_students(db: Session):
    return db.query(models.Student).all()

# READ ONE
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

# UPDATE
def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = get_student(db, student_id)
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.grade = student.grade
        db.commit()
        db.refresh(db_student)
    return db_student

# DELETE
def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student