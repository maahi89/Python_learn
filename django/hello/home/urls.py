from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),       # when we type / it will execute the index function in views.py
    path("about/", views.about, name="about"), # about page will execute the about function in views.py
    path("services/", views.services, name="services"), # services page will execute the services function in views.py
    path("contact/" , views.contact, name="contact") # contact page will execute the contact function in views.py
]