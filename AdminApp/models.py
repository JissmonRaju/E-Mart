from django.db import models

# Create your models here.

class Category(models.Model):
    C_Name = models.CharField(max_length=100,null=True,blank=True)
    C_Desc = models.CharField(max_length=150,null=True,blank=True)
    C_Image = models.ImageField(upload_to="Category Image",blank=True,null=True)

class Product(models.Model):
    PC_Name = models.CharField(max_length=100,null=True,blank=True)
    P_Name = models.CharField(max_length=100,null=True,blank=True)
    P_Quant = models.IntegerField(null=True,blank=True)
    P_Price = models.IntegerField(null=True,blank=True)
    P_Desc = models.CharField(max_length=150,null=True,blank=True)
    P_Image = models.ImageField(upload_to="Product Image",null=True,blank=True)

