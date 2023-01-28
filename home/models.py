from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    desc = models.TextField(max_length=500)
    # date = models.DateField()   

    def __str__(self):
        return self.name

class Login(models.Model):
    Name = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

