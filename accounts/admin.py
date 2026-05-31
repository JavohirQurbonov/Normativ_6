from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {
            "fields": ("phone_number", "birth_date",'role')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('role',)
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)



