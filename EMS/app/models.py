from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    empid = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=13)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
