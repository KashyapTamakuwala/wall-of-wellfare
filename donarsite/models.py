from django.db import models
from login.models import User
from ngo.models import needs
# Create your models here.

class accepteddonations(models.Model):
    dname=models.ForeignKey(User,db_column="username",on_delete=models.CASCADE)
    dtype=models.CharField(max_length=20)
    nmame=models.CharField(max_length=100)
    date=models.DateField(null=True)
    status=models.CharField(max_length=1)

