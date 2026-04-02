from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),       # when we type / it will execute the index function in views.py
    path("about/", views.about, name="about"), # about page will execute the about function in views.py
    path("services/", views.services, name="services"), # services page will execute the services function in views.py
    path("contact/" , views.contact, name="contact"), # contact page will execute the contact function in views.py
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('update-student/<int:id>/', views.update_student, name='update_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]