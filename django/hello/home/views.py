from django.shortcuts import render, HttpResponse, redirect
from .models import Student, Employee
from .forms import EmployeeForm, StudentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):

    student_form = StudentForm()
    form = EmployeeForm()

    if request.method == "POST":

        # 👉 STUDENT FORM SUBMIT
        if 'student_submit' in request.POST:
            student_form = StudentForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                return redirect('home')

        # 👉 EMPLOYEE FORM SUBMIT
        elif 'employee_submit' in request.POST:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')

    data = {
        "form": form,
        "student_form": student_form,
        "employees": Employee.objects.all(),
        "students": Student.objects.all(),

        # existing data
        "name": "Mahitha",
        "age": 22,
        "hobbies": ["Coding", "Chess", "Learning"],
        "fav_color": ["Black", "Blue", "White"]
    }

    return render(request, 'index.html', data)

def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')

def update_employee(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == "POST":
        emp.name = request.POST['name']
        emp.age = request.POST['age']
        emp.email = request.POST.get('email')
        emp.salary = request.POST['salary']
        emp.designation = request.POST['designation']
        emp.save()
        return redirect('home')

    return render(request, 'update_employee.html', {'emp': emp})

def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('home')

def about(request):
    data = {
        "about_me" : "i am a software developer and i love to learn new technologies and i am passionate about coding and i want to become a full stack developer in future"
    }
    return render(request, 'about.html', data)
    #  return HttpResponse("You're at the services page.")


def services(request):
    return HttpResponse("You're at the services page.")

def contact(request):
    data = {
        "number": 1234567890,
        "name": "Mahitha",
        "mail": "mahitha@example.com"
    }
    return render(request, 'contact.html', data)


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists ❌")

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials ❌")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')