from django.contrib import admin

from .models import User
from .models import UserInfo
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","phone_number","email"]
    class Meta:
        model = User
admin.site.register(User, UserAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","first_name","last_name","points"]
    class Meta:
        model = UserInfo
admin.site.register(UserInfo, UserInfoAdmin)