from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Reg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    gender=models.CharField(max_length=100)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=30)

class Product(models.Model):
    
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.IntegerField(max_length=100)
    image=models.ImageField(upload_to ='images/')
    status=models.CharField(max_length=10)
    
