from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task, SubTask
from .forms import ProjectForm, TaskForm, SubTaskForm

def project_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        projects = Project.objects.filter(
            name__icontains=search_query
        ) | Project.objects.filter(
            description__icontains=search_query
        )
    else:
        projects = Project.objects.all()

    return render(request, 'taskly/project_list.html', {
        'projects': projects,
        'search_query': search_query
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'taskly/project_detail.html', {'project': project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskly:project_list')
    else:
        form = ProjectForm()
    return render(request, 'taskly/project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('taskly:project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'taskly/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('taskly:project_list')
    return render(request, 'taskly/project_confirm_delete.html', {'project': project})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskly/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskly:project_list')
    else:
        form = TaskForm()
    return render(request, 'taskly/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskly:task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskly/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('taskly:project_list')
    return render(request, 'taskly/task_confirm_delete.html', {'task': task})

def subtask_detail(request, pk):
    subtask = get_object_or_404(SubTask, pk=pk)
    return render(request, 'taskly/subtask_detail.html', {'subtask': subtask})

def subtask_create(request):
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskly:project_list')
    else:
        form = SubTaskForm()
    return render(request, 'taskly/subtask_form.html', {'form': form})

def subtask_update(request, pk):
    subtask = get_object_or_404(SubTask, pk=pk)
    if request.method == 'POST':
        form = SubTaskForm(request.POST, instance=subtask)
        if form.is_valid():
            form.save()
            return redirect('taskly:subtask_detail', pk=subtask.pk)
    else:
        form = SubTaskForm(instance=subtask)
    return render(request, 'taskly/subtask_form.html', {'form': form})

def subtask_delete(request, pk):
    subtask = get_object_or_404(SubTask, pk=pk)
    if request.method == 'POST':
        subtask.delete()
        return redirect('taskly:project_list')
    return render(request, 'taskly/subtask_confirm_delete.html', {'subtask': subtask})
