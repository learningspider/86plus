# -*- coding: utf8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from plus86.models import memberCard,UserProfile,clothes,gonggao,huodong,riqiqiandao,guanzhuClothesModel
from plus86.models import foods,huodong,jianyi,jiangpin,riqiqiandaopre
from django.contrib.auth.admin import UserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    
class gonggaoAdmin(admin.ModelAdmin):
    list_display = ('id','ggname', 'ggtime', 'istimeout')
    search_fields = ('ggname',)

class clothesAdmin(admin.ModelAdmin):
    list_display = ('id','clname', 'clcity', 'clshi','cltime')
    search_fields = ('clname',)

class foodsAdmin(admin.ModelAdmin):
    list_display = ('id','fdname', 'fdcity', 'fdshi')
    search_fields = ('fdname',)

class guanzhuClothesAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'gzClothes','gztime')
    search_fields = ('username',)

class huodongAdmin(admin.ModelAdmin):
    list_display = ('id','hdcompany', 'hdname','hdtime','istimeout')
    search_fields = ('hdcompany',)

class jianyiAdmin(admin.ModelAdmin):
    list_display = ('id','jyusername', 'jyuser','jyqq','jyphone','jyip','jytime')
 
#奖品   
class jiangpinAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'jplevel','jp','jptime')
    search_fields = ('username','jp')
    
#日期签到   
class riqiqiandaoAdmin(admin.ModelAdmin):
    list_display = ('id','yonghu', 'tianshu')
    search_fields = ('yonghu',)

#上月日期签到   
class riqiqiandaopreAdmin(admin.ModelAdmin):
    list_display = ('id','yonghu', 'tianshu','ischoujiang')
    search_fields = ('yonghu',)

admin.site.register(memberCard)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(clothes,clothesAdmin)
admin.site.register(foods,foodsAdmin)
admin.site.register(gonggao,gonggaoAdmin)
admin.site.register(huodong,huodongAdmin)
admin.site.register(riqiqiandao,riqiqiandaoAdmin)
admin.site.register(riqiqiandaopre,riqiqiandaopreAdmin)
admin.site.register(guanzhuClothesModel,guanzhuClothesAdmin)
admin.site.register(jianyi,jianyiAdmin)
admin.site.register(jiangpin,jiangpinAdmin)
