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
    clname=models.CharField(max_length=100,verbose_name='服饰公司名')
    #clurl=models.CharField(max_length=60)
    clcity=models.CharField(max_length=60,verbose_name='省',blank=True)
    clshi=models.CharField(max_length=60,verbose_name='市',blank=True)
    tpurl=models.CharField(max_length=100,verbose_name='图片地址')
    clinfo=models.TextField(verbose_name='服饰详情')
    cltime=models.DateTimeField(verbose_name='创建时间')
    
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='服饰列表'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='服饰'#修改管理级页面显示
    
    def __unicode__(self):
        return self.clname



#服饰分类模块
class foods(models.Model):
    fdname=models.CharField(max_length=100,verbose_name='美食公司名')
    #clurl=models.CharField(max_length=60)
    fdcity=models.CharField(max_length=60,verbose_name='省',blank=True)
    fdshi=models.CharField(max_length=60,verbose_name='市',blank=True)
    tpurl=models.CharField(max_length=100,verbose_name='图片地址')
    fdinfo=models.TextField(verbose_name='美食详情')
    
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='美食列表'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='美食'#修改管理级页面显示
    
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
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='公告内容'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='公告'#修改管理级页面显示
    def __unicode__(self):
        return self.ggname

#服饰关注
class guanzhuClothesModel(models.Model):
    """关注
    """
    username=models.CharField(max_length=60,verbose_name='用户名')
    gzClothes=models.CharField(max_length=100,verbose_name='关注公司')
    gzurl=models.CharField(max_length=100,verbose_name='关注公司url')
    gztpurl=models.CharField(max_length=100,verbose_name='图片url')
    gztime=models.DateTimeField(auto_now_add=True,verbose_name='关注时间')
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='关注列表'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='关注'#修改管理级页面显示
    def __unicode__(self):
        return self.username

#活动
class huodong(models.Model):
    hdcompany=models.CharField(max_length=100,verbose_name='公司名称')
    hdname=models.CharField(max_length=60,verbose_name='活动名称')
    hdinfo=models.TextField(verbose_name='活动信息')
    hdtime=models.DateTimeField(verbose_name='活动创建时间')
    hdtpurl=models.CharField(max_length=100,verbose_name='图片url')
    istimeout=models.BooleanField(verbose_name='是否过期')
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='活动列表'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='活动'#修改管理级页面显示
    
    def __unicode__(self):
        return self.hdname

#投诉建议
class jianyi(models.Model):
    jyusername=models.CharField(max_length=60,verbose_name='用户名')
    jyuser=models.CharField(max_length=60,verbose_name='联系人')
    jyqq=models.CharField(max_length=60,verbose_name='QQ号')
    jyphone=models.CharField(max_length=11,verbose_name='手机号')
    jyinfo=models.TextField(max_length=2000,verbose_name='建议内容')
    jyip=models.CharField(max_length=60,verbose_name='IP地址')
    jytime=models.DateTimeField(auto_now_add=True,verbose_name='时间')
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='投诉建议列表'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='投诉建议'#修改管理级页面显示
    
    def __unicode__(self):
        return self.jyusername
  
 #中奖列表
class jiangpin(models.Model):
    username=models.CharField(max_length=60,verbose_name='用户名')
    jplevel=models.CharField(max_length=60,verbose_name='奖品等级')
    jp=models.CharField(max_length=100,verbose_name='奖品')
    jptime=models.DateTimeField(auto_now_add=True,verbose_name='时间')
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='奖品列表'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='奖品'#修改管理级页面显示
    
    def __unicode__(self):
        return self.username 
    
#日期签到
class riqiqiandao(models.Model):
    yonghu=models.CharField(max_length=60,verbose_name='用户名')
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
    tianshu=models.IntegerField(default=0,verbose_name='签到天数')
    ischoujiang=models.BooleanField(verbose_name='是否已抽奖')
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='签到详情'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='签到'#修改管理级页面显示
    def __unicode__(self):
        return self.yonghu

#上个月日期签到
class riqiqiandaopre(models.Model):
    yonghu=models.CharField(max_length=60,verbose_name='用户名')
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
    tianshu=models.IntegerField(default=0,verbose_name='签到天数')
    ischoujiang=models.BooleanField(verbose_name='是否已抽奖')
    class Meta:
        #db_table = 'Product'#数据库名
        verbose_name='上月签到详情'#修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural='上月签到'#修改管理级页面显示
    def __unicode__(self):
        return self.yonghu
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phonenumber = models.CharField(max_length=11,unique=False)
    IDcard = models.CharField(max_length=18,unique=False)
    openid = models.CharField(max_length=60,unique=False)
    
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
  
post_save.connect(create_user_profile, sender=User)
    
