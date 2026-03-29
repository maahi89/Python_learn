from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    salary = models.FloatField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name