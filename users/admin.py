from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'profile_photo')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'has_profile_photo')
    list_filter = BaseUserAdmin.list_filter + ('role',)
    
    def has_profile_photo(self, obj):
        return bool(obj.profile_photo)
    has_profile_photo.short_description = 'Profile Photo'
    has_profile_photo.boolean = True
