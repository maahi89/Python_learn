from sqlalchemy import Column, Integer, String
from database import Base
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(50))
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    department = Column(String(100))
    designation = Column(String(100))
    salary = Column(Integer)
    location = Column(String(100))
    experience = Column(Integer)
    joining_date = Column(String(50))

    