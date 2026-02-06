class Student:
    def __init__(self, roll_no, name, marks, age):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.age = age

    def total(self):
        return sum(self.marks)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("roll no:", self.roll_no)
        print("name:", self.name)
        print("marks:", self.marks)
        print("total:", self.total())
        print("average:", self.average())
        print("age:", self.age)

students = []
def add_student():
    roll_no=int(input("Enter roll number:"))
    name=input("enter student name: ")
    marks=list(map(float, input("enter marks separated by space: ").split()))
    age=int(input("enter student age: "))
    students.append(Student(roll_no, name, marks, age))

def display_students():
    if not students:
        print("no student found")
    else:
        for s in students:
            s.display()

def search_student():
    name=input("enter the student name to serch: ")
    if not students:
        print("No student found")
        return
    for s in students:
        if s.name == name:
            print(f"{name} found")
            print("roll_no:", s.roll_no)
            print("marks:", s.marks)
            print("total:", s.total())
            print("average:", s.average())
            print("age:", s.age)
            return
    print(f"{name} not found")

def delete_student():
    name=input("enter the student name to delete ")
    if not students:
        print("no student found")
        return
    for s in students:
        if s.name == name:
            students.remove(s)
            print(f"{name} deleted successfully")
            return
    print(f"{name} not found")

while True:
    print("\n student management system menu")
    print("1. add student")
    print("2. display students")
    print("3. search student")
    print("4. delete student")
    print("5. exit")
    choice=int(input("enter your choice 1/2/3/4/5: "))
    if choice==1:
        add_student()
    elif choice==2:
        display_students()
    elif choice==3:
        search_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        print("exiting the program")
        break
    else:
        print("invalid choice")            


