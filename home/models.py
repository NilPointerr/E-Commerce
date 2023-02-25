from django.db import models
from django import forms

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    desc = models.TextField(max_length=500)
    # date = models.DateField()   

    def __str__(self):
        return self.name

class Login(models.Model):
    Name = models.CharField(max_length=200,blank=False)
    password = models.CharField(max_length=50,blank=False)

   

    def __str__(self):
        return self.Name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to='static/images')


    def __str__(self):
        return self.product_name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_Json= models.CharField(max_length=5000,default="")
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address1=models.CharField(max_length=111,default="")
    address2 = models.CharField(max_length=200,default="")
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name 
