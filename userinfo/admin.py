from django.contrib import admin
from . import models
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname','uemail','udate']
    list_filter = ['uname','udate']

admin.site.register(models.UserInfo,UserInfoAdmin)