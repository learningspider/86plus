# -*- coding: utf8 -*-
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
    #clurl=models.CharField(max_length=60)
    clcity=models.CharField(max_length=60)
    clshi=models.CharField(max_length=60)
    tpurl=models.CharField(max_length=60)
    clinfo=models.TextField()
    
    
    def __unicode__(self):
        return self.clname

#公告
class gonggao(models.Model):
    """公告
    """
    ggname=models.CharField(max_length=60,verbose_name='公告名称')
    gginfo=models.TextField(verbose_name='公告内容')
    ggtime=models.DateTimeField(verbose_name='公告创建时间')
    istimeout=models.BooleanField(verbose_name='是否过期')
    
    def __unicode__(self):
        return self.ggname

#公告
class huodong(models.Model):
    hdname=models.CharField(max_length=60)
    hdinfo=models.TextField()
    hdtime=models.DateTimeField()
    istimeout=models.BooleanField()
    def __unicode__(self):
        return self.hdname
    
#日期签到
class riqiqiandao(models.Model):
    yonghu=models.CharField(max_length=60)
    h1=models.CharField(max_length=2)
    h2=models.CharField(max_length=2)
    h3=models.CharField(max_length=2)
    h4=models.CharField(max_length=2)
    h5=models.CharField(max_length=2)
    h6=models.CharField(max_length=2)
    h7=models.CharField(max_length=2)
    h8=models.CharField(max_length=2)
    h9=models.CharField(max_length=2)
    h10=models.CharField(max_length=2)
    h11=models.CharField(max_length=2)
    h12=models.CharField(max_length=2)
    h13=models.CharField(max_length=2)
    h14=models.CharField(max_length=2)
    h15=models.CharField(max_length=2)
    h16=models.CharField(max_length=2)
    h17=models.CharField(max_length=2)
    h18=models.CharField(max_length=2)
    h19=models.CharField(max_length=2)
    h20=models.CharField(max_length=2)
    h21=models.CharField(max_length=2)
    h22=models.CharField(max_length=2)
    h23=models.CharField(max_length=2)
    h24=models.CharField(max_length=2)
    h25=models.CharField(max_length=2)
    h26=models.CharField(max_length=2)
    h27=models.CharField(max_length=2)
    h28=models.CharField(max_length=2)
    h29=models.CharField(max_length=2)
    h30=models.CharField(max_length=2)
    h31=models.CharField(max_length=2) 
    def __unicode__(self):
        return self.yonghu
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phonenumber = models.CharField(max_length=11,unique=True)
    IDcard = models.CharField(max_length=18,unique=True)
    openid = models.CharField(max_length=60,unique=True)
    
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
  
post_save.connect(create_user_profile, sender=User)
    
