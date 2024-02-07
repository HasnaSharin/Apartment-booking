from django.db import models

# Create your models here.
class RegisterDb(models.Model):
    UserName=models.CharField(max_length=50,null=True,blank=True)
    UEmail=models.EmailField(max_length=60,null=True,blank=True)
    UPassword=models.CharField(max_length=60,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    UsImage=models.ImageField(upload_to="userimage",null=True,blank=True)
class BookingDb(models.Model):
    BookingName=models.CharField(max_length=100,null=True,blank=True)
    PhoneB=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Members=models.IntegerField(null=True,blank=True)

