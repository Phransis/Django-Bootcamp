from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.view_post, name='view_post'),
    path('post/new/', views.create_post, name='post_create'),
    path('post/<int:pk>/edit/', views.edit_post, name='post_update'),
    path('post/<int:pk>/delete/', views.delete_post, name='post_delete'),
    path('authors/', views.author_list, name='author_list'),
    path('author/<int:pk>/', views.view_author, name='author_detail'),
    path('author/new/', views.create_author, name='author_create'),
    path('author/<int:pk>/edit/', views.edit_author, name='author_update'),
    path('author/<int:pk>/delete/', views.delete_author, name='author_delete'),
    path('technology/', views.technology_posts, name='technology_posts'),
    path('lifestyle/', views.lifestyle_posts, name='lifestyle_posts'),
    path('travel/', views.travel_posts, name='travel_posts'),
    path('food/', views.food_posts, name='food_posts'),
]
