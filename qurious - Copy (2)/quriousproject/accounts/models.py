
from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractUser
class Member(models.Model):
    id=models.AutoField(primary_key=True)
    phone =models.BigIntegerField(default=0)
    email= models.CharField(max_length=20,default='@gmail.com')
    username=models.CharField(max_length=30,null=False,default='admin99@club')
    password=models.CharField(max_length=20,null=False,default='admin123')

    first_name=models.CharField(max_length=20,verbose_name="first_name")
    last_name=models.CharField(max_length=20,verbose_name="last_name")

    user_type= models.CharField(max_length=20,default='admin')
    address = models.CharField(max_length=100,verbose_name="address")
    city=models.CharField(max_length=50,verbose_name="city")
    date_of_birth=models.DateField(auto_now=False)

    passportnumber =models.BigIntegerField(default=0)
    profile_photo=models.ImageField(upload_to="profile/",max_length=300)
    passport_expiry_date=models.DateField(default="DD-MM-YYYY")
    
    # user=models.ForeignKey(to=User,on_delete=models.CASCADE)


