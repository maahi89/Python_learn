class person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno=rollno
s1 = student(*input("Enter name, age and rollno of student: ").split())
print("Name: ", s1.name)
print("Age: ", s1.age)          
print("Rollno: ", s1.rollno)
    