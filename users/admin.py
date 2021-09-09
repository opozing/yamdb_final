from django import forms
from django.contrib import admin
from django.db import models

from users.models import YamdbUser


@admin.register(YamdbUser)
class YamdbUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name',
                    'role', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name',)
    list_filter = ('role',)
    empty_value_display = '-not filled-'
    list_display_links = ('pk', 'email',)
    date_hierarchy = 'last_login'

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'username', 'email', 'bio',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('role', 'date_joined', 'last_login',
                       'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea},
    }
