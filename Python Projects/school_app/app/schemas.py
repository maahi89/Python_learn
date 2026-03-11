from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    grade: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True

