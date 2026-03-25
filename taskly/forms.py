from django import forms
from .models import Project, Task, SubTask

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'start_date', 'end_date']

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['task', 'title', 'start_date', 'end_date']