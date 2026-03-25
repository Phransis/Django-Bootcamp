from urllib import request

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Author, Post
from .forms import PostForm

# Create your views here.
def landing_page(request):
    instance = Post.objects.order_by('-created_at')[:5]
    return render(request, 'blog/landing_page.html', {'posts': instance})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:landing_page')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def view_post(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    context = {
        'post': instance,}
    return render(request, 'blog/view_post.html', context)

def edit_post(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('blog:view_post', pk=instance.pk)
    else:
        form = PostForm(instance=instance)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': instance})

def delete_post(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    return redirect('blog:landing_page')

def post_list(request):
    return render(request, 'blog/post_list.html')

def author_list(request):
    return render(request, 'blog/author_list.html')

def view_author(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    context = {
        'post': instance,}
    return render(request, 'blog/author_detail.html', context)

def create_author(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:landing_page')
    else:
        form = PostForm()
    return render(request, 'blog/create_author.html', {'form': form})

def edit_author(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('blog:view_post', pk=instance.pk)
    else:
        form = PostForm(instance=instance)
    return render(request, 'blog/edit_author.html', {'form': form, 'post': instance})

def delete_author(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    return redirect('blog/delete_author.html')

def technology_posts(request):
    posts = Post.objects.filter(category='TECHNOLOGY')
    return render(request, 'blog/technology_posts_page.html', {'posts': posts})

def lifestyle_posts(request):
    posts = Post.objects.filter(category='LIFESTYLE')
    return render(request, 'blog/lifestyle_posts_page.html', {'posts': posts})

def travel_posts(request):
    posts = Post.objects.filter(category='TRAVEL')
    return render(request, 'blog/travel_posts_page.html', {'posts': posts})

def food_posts(request):
    posts = Post.objects.filter(category='FOOD')
    return render(request, 'blog/food_posts_page.html', {'posts': posts})

