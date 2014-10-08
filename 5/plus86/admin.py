from django.contrib import admin
from django.contrib.auth.models import User
from plus86.models import memberCard,UserProfile,clothes,gonggao,huodong,riqiqiandao,guanzhuClothesModel
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
    list_display = ('id','clname', 'clcity', 'clshi')
    search_fields = ('clname',)

class guanzhuClothesAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'gzClothes')
    search_fields = ('username',)

admin.site.register(memberCard)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(clothes,clothesAdmin)
admin.site.register(gonggao,gonggaoAdmin)
admin.site.register(huodong)
admin.site.register(riqiqiandao)
admin.site.register(guanzhuClothesModel,guanzhuClothesAdmin)
