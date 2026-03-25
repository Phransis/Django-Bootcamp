from django.urls import path
from . import views

app_name = 'taskly'
urlpatterns = [
    path('', views.project_list, name='project_list'),  
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('subtask/<int:pk>/', views.subtask_detail, name='subtask_detail'),  
    path('subtask/new/', views.subtask_create, name='subtask_create'),  
    path('subtask/<int:pk>/edit/', views.subtask_update, name='subtask_update'),
    path('subtask/<int:pk>/delete/', views.subtask_delete, name='subtask_delete'),
]