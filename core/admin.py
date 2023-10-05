from django.contrib import admin
from .models import Images, CustomUser, AccountTiers, ThumbnailsSize, Thumbnail
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = CustomUser
    list_display = ["username", "account_tiers"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("account_tiers",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("account_tiers",)}),)


class ThumbnailAdmin(admin.ModelAdmin):
    model= Thumbnail
    list_display = ["id", "image"]

class ImagesAdmin(admin.ModelAdmin):
    model= Thumbnail
    list_display = ["id"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(AccountTiers)
admin.site.register(ThumbnailsSize)
admin.site.register(Thumbnail, ThumbnailAdmin)







