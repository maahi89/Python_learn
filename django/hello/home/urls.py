from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),       # homepage
    path("about/", views.about, name="about"), # about page
    path("services/", views.services, name="services") # services page

]