from django.db import models
from login.models import User
# Create your models here.

class needs(models.Model):
    ntype=models.CharField(max_length=20)
    description=models.TextField(max_length=10)
    nname=models.ForeignKey(User,db_column='username',on_delete=models.CASCADE)
    status=models.CharField(max_length=1)