from django.contrib import admin
from django.contrib.auth.models import Group
from accounts.models import User, UserRole
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


#class UserAdmin(BaseUserAdmin):

admin.site.register(User)
admin.site.register(UserRole)
admin.site.unregister(Group)
