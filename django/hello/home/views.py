from django.shortcuts import render, HttpResponse
from .models import Student , Employee



def index(request):
    data = {
        "name": "Mahitha",
        "age": 20,
        "hobbies": ["coding", "reading", "traveling"],
        "fav_color": ["blue", "green", "red"],
        "students": Student.objects.all(), # this will fetch all the students from the database and pass it to the template
        "employees": Employee.objects.all() # this will fetch all the employees from the database and pass it to the template
    }
    return render(request, 'index.html', data) # this will look for index.html file in templates folder and render it


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


