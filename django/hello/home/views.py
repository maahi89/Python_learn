from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You're at the home index.")
def about(request):
    return HttpResponse("You're at the about page.")