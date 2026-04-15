from django.shortcuts import render
from django.views.generic import ListView
from makola.models import Profile

# Create your views here.

def homepage(request):
    return render(request, 'makola/homepage.html')

class ProfileListView(ListView):
    model = Profile
    template_name = 'makola/profile_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(ListView):
    model = Profile
    template_name = 'makola/profile_detail.html'
    context_object_name = 'profile'

class ProfileCreateView(ListView):
    model = Profile
    template_name = 'makola/profile_create.html'
    context_object_name = 'profile'
    success_url = '/profiles/'  # Redirect to profile list after successful creation

class ProfileUpdateView(ListView):
    model = Profile
    template_name = 'makola/profile_update.html'
    context_object_name = 'profile'
    success_url = '/profiles/'  # Redirect to profile list after successful update

class ProfileDeleteView(ListView):
    model = Profile
    template_name = 'makola/profile_delete.html'
    context_object_name = 'profile'
    message = 'Are you sure you want to delete this profile?'
    success_url = '/profiles/'  # Redirect to profile list after successful deletion

class ProductListView(ListView):
    model = Profile
    template_name = 'makola/product_list.html'
    context_object_name = 'products'

class ProductDetailView(ListView):
    model = Profile
    template_name = 'makola/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(ListView):
    model = Profile
    template_name = 'makola/product_create.html'
    context_object_name = 'product'
    success_url = '/products/'  # Redirect to product list after successful creation

class ProductUpdateView(ListView):
    model = Profile
    template_name = 'makola/product_update.html'
    context_object_name = 'product'
    success_url = '/products/'  # Redirect to product list after successful update

class ProductDeleteView(ListView):
    model = Profile
    template_name = 'makola/product_delete.html'
    context_object_name = 'product'
    message = 'Are you sure you want to delete this product?'
    success_url = '/products/'  # Redirect to product list after successful deletion
    

class CategoryListView(ListView):
    model = Profile
    template_name = 'makola/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(ListView):
    model = Profile
    template_name = 'makola/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(ListView):
    model = Profile
    template_name = 'makola/category_create.html'
    context_object_name = 'category'
    success_url = '/categories/'  # Redirect to category list after successful creation

class CategoryUpdateView(ListView):
    model = Profile
    template_name = 'makola/category_update.html'
    context_object_name = 'category'
    success_url = '/categories/'  # Redirect to category list after successful update

class CategoryDeleteView(ListView):
    model = Profile
    template_name = 'makola/category_delete.html'
    context_object_name = 'category'
    message = 'Are you sure you want to delete this category?'
    success_url = '/categories/'  # Redirect to category list after successful deletion

