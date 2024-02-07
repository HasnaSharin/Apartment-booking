from django.db import models


# Create your models here.
class apartmentDb(models.Model):
    Aname=models.CharField(max_length=100,null=True,blank=True)
    Oname=models.CharField(max_length=50,null=True,blank=True)
    Category=models.CharField(max_length=100,null=True,blank=True)

    Image=models.ImageField(upload_to="profile",null=True,blank=True)
    Description=models.CharField(max_length=150,null=True,blank=True)
class Types_Ap(models.Model):
    Category=models.CharField(max_length=50,null=True,blank=True)
    Company_Name=models.CharField(max_length=60,null=True,blank=True)
    Price=models.CharField(max_length=50,null=True,blank=True)
    Types=models.CharField(max_length=100,null=True,blank=True)
    Area=models.CharField(max_length=100,null=True,blank=True)
    Type_Image=models.ImageField(upload_to="Dp",null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)

class ContactDb(models.Model):
    Name=models.CharField(max_length=60,null=True,blank=True)
    Email=models.EmailField(max_length=70,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=150,null=True,blank=True)

