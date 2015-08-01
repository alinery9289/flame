
from django.db import models

# Create your models here.
class user(models.Model):
    authcode = models.CharField(max_length=32,primary_key=True,unique=True)
    email = models.CharField(max_length=45,unique=True)
    userid = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=32)
    userstorage = models.IntegerField(max_length=8)
    secretkey = models.CharField(max_length=45,unique=True,blank=True,null=True)
    outdate = models.DateTimeField(blank=True,null=True)