from django.contrib import admin

from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'role', 'is_active',  'last_login',)
    list_ordering = ('-date_joined',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
