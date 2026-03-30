from django.shortcuts import render, HttpResponse, redirect
from .models import Student , Employee

def index(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST.get('email'),
            salary=request.POST['salary'],
            designation=request.POST['designation']
        )
        return redirect('home')

    data = {
        "name": "Mahitha",
        "age": 20,
        "hobbies": ["coding", "reading", "traveling"],
        "fav_color": ["blue", "green", "red"],
        "students": Student.objects.all(),
        "employees": Employee.objects.all()
    }

    return render(request, 'index.html', data)

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


