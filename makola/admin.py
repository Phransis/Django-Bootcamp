from django.contrib import admin

# Register your models here.

from .models import Profile, Product, Category, Shop

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'user_type', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('user_type', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at', 'image')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'description')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('owner', 'created_at')