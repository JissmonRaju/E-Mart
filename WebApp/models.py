from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=150,null=True,blank=True)

class Register(models.Model):
    User_Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,blank=True,null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    PassWord = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,blank=True,null=True)

class CartDB(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)
    Product_Image = models.ImageField(upload_to="Cart Images", null=True, blank=True)


class OrderDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=150,null=True,blank=True)
    Address = models.CharField(max_length=200,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Pin = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=250,null=True,blank=True)