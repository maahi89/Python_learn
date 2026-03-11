from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    email: str
    phone: str
    department: str
    designation: str
    salary: int
    location: str
    experience: int
    joining_date: str