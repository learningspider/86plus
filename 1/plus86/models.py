from django.db import models

# Create your models here.
class memberCard(models.Model):
    openid = models.CharField(max_length=60,unique=True)
    phonenumber = models.CharField(max_length=11,unique=True)
    name = models.CharField(max_length=60) #email
    IDcard = models.CharField(max_length=18,unique=True)
    username = models.CharField(max_length=10)
    
class user(models.Model):
    username = models.CharField(max_length=60,primary_key=True)
    verify = models.IntegerField(unique=True)