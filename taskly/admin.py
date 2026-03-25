from django.contrib import admin
from .models import Project, Task, SubTask

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'num_of_tasks', 'is_completed', 'created_at', 'start_date', 'end_date')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('name', 'description')

admin.site.register(Project, ProjectAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'description', 'is_assigned', 'created_at', 'is_completed', 'start_date', 'end_date')
    list_filter = ('is_assigned', 'is_completed', 'created_at')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'is_completed', 'is_assigned', 'created_at', 'start_date', 'end_date')
    list_filter = ('is_completed', 'is_assigned', 'created_at')
    search_fields = ('title',)

admin.site.register(SubTask, SubTaskAdmin)
