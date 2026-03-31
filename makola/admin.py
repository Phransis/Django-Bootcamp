from django.contrib import admin

# Register your models here.

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'user_type', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('user_type', 'created_at')
    