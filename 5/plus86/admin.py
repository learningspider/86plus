from django.contrib import admin
from django.contrib.auth.models import User
from plus86.models import memberCard,UserProfile,clothes,gonggao,huodong,riqiqiandao
from django.contrib.auth.admin import UserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    
class gonggao(admin.ModelAdmin):
    list_display = ('ggname', 'ggtime', 'istimeout')
    search_fields = ('ggname')

admin.site.register(memberCard)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(clothes)
admin.site.register(gonggao)
admin.site.register(huodong)
admin.site.register(riqiqiandao)
