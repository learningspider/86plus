from django.contrib import admin
from django.contrib.auth.models import User
from plus86.models import memberCard,UserProfile
from django.contrib.auth.admin import UserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.register(memberCard)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)