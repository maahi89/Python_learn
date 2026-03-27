from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("You're at the home index.")

def about(request):
    return HttpResponse("You're at the about page.")

def services(request):
    return HttpResponse("You're at the services page.")