from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("You're at the home index.")
    return render(request, 'index.html') # this will look for index.html file in templates folder and render it

def about(request):
    return HttpResponse("You're at the about page.")

def services(request):
    return HttpResponse("You're at the services page.")

def contact(request):
    return HttpResponse("You're at the contact page.")


