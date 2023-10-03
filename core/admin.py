from django.contrib import admin
from .models import Images, CustomUser 
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm

admin.site.register(Images)

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = CustomUser
    list_display = ["username", "account_tiers"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("account_tiers",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("account_tiers",)}),)




admin.site.register(CustomUser, CustomUserAdmin)




