from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models import UserProfile

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "is_staff",
        "is_active",
        "first_name",
        "last_name",
        "role",
    )
    ordering = ("-date_joined", )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
