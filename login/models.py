from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
#Create your models here.
# class donar(models.Model):
#     id=models.AutoField(primary_key=True)
#     username=models.ForeignKey('USER',on_delete=models.CASCADE)
#     First_name=models.CharField(max_length=30)
#     Last_name=models.CharField(max_length=30)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     Contact= models.CharField(validators=[phone_regex], max_length=17, blank=True)
#     Address=models.CharField(max_length=50)
#     City=models.CharField(max_length=20)
#     State=models.CharField(max_length=10)
#     Email_id=models.EmailField(max_length=70,unique=True,null=False)
#     Password=models.CharField(max_length=10)


# class NGO(models.Model):
#     id=models.AutoField(primary_key=True)
#     username=models.ForeignKey('USER',on_delete=models.CASCADE)
#     Organization=models.CharField(max_length=30)
#     Owner_First_name=models.CharField(max_length=30)
#     Owner_Last_name=models.CharField(max_length=30)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     Contact= models.CharField(validators=[phone_regex], max_length=17, blank=True)
#     Address=models.CharField(max_length=50)
#     City=models.CharField(max_length=20)
#     State=models.CharField(max_length=10)
#     Email_id=models.EmailField(max_length=70,unique=True,null=False)
#     Password=models.CharField(max_length=10)

# class USER(models.Model):
#     name=models.CharField(max_length=30)
#     utype=models.CharField(max_length=5)

# class test(models.Model):
#     name=models.CharField(max_length=20)

class User(AbstractUser):
    type=models.TextField(max_length=5)

class details(models.Model):
    username=models.ForeignKey(User,db_column="username",on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Contact= models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Address=models.CharField(max_length=50)
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=10)

User=get_user_model()