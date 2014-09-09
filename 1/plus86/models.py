from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class memberCard(models.Model):
    openid = models.CharField(max_length=60,unique=True)
    phonenumber = models.CharField(max_length=11,unique=True)
    name = models.CharField(max_length=60) #email
    IDcard = models.CharField(max_length=18,unique=True)
    username = models.CharField(max_length=10)
    
class user(models.Model):
    username = models.CharField(max_length=60,primary_key=True)
    verify = models.CharField(max_length=60)

#服饰分类模块
class clothes(models.Model):
    clname=models.CharField(max_length=60)
    clurl=models.CharField(max_length=60)
    clcity=models.CharField(max_length=60)
    tpurl=models.CharField(max_length=60)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phonenumber = models.CharField(max_length=11,unique=True)
    IDcard = models.CharField(max_length=18,unique=True)
    openid = models.CharField(max_length=60,unique=True)
    
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
  
post_save.connect(create_user_profile, sender=User)
    
