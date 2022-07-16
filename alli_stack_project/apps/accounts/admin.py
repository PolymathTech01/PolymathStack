from typing import Any, List
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from . import forms
# Register your models here.


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form: Any = forms.CustomUserCreationForm
    form: Any = forms.CustomUserChangeForm
    ordering = ['email']
    list_display = ['email', 'is_staff', 'is_active', 'is_superuser']
    search_fields: List[str] = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Details', {'fields': ('first_name', 'last_name', 'slug')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})

    )
