from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class AccountAdmin(UserAdmin):
    list_display = ('pk', 'email', 'is_admin')
    search_fields = ('pk', 'email', 'is_admin')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, AccountAdmin)