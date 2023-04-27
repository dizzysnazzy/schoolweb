from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    units = models.ManyToManyField(Unit)

    def __str__(self):
        return self.user.username
 

