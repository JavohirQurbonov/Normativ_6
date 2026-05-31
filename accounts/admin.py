from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {
            "fields": ("phone_number", "birth_date")
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)