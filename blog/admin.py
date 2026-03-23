from django.contrib import admin

# Register your models here.
from .models import Author
from .models import Post

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author
    list_display = ('name', 'email', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'email')

admin.site.register(Author, AuthorAdmin)