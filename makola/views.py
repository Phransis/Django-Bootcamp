from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from makola.models import Category, Product, Profile

# Create your views here.

def homepage(request):
    return render(request, 'makola/homepage.html')

class ProfileListView(ListView):
    model = Profile
    template_name = 'makola/profile_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'makola/profile_detail.html'
    context_object_name = 'profile'

class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'makola/profile_create.html'
    fields = ['name', 'username', 'phone_number', 'email', 'password', 'address', 'bio', 'user_type']
    context_object_name = 'profile'
    success_url = reverse_lazy('makola:list-profiles')  # Redirect to profile list after successful creation

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'makola/profile_edit.html'
    fields = ['name', 'phone_number', 'address', 'bio', 'user_type']
    context_object_name = 'profile'
    success_url = reverse_lazy('makola:list-profiles')  # Redirect to profile list after successful update

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'makola/profile_delete.html'
    context_object_name = 'profile'
    message = 'Are you sure you want to delete this profile?'
    success_url = reverse_lazy('makola:list-profiles')  # Redirect to profile list after successful deletion

class ProductListView(ListView):
    model = Product
    template_name = 'makola/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'makola/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'makola/product_create.html'
    fields = ['name', 'description', 'price', 'category']
    context_object_name = 'product'
    success_url = reverse_lazy('makola:list-products')  # Redirect to product list after successful creation

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'makola/product_update.html'
    fields = ['name', 'description', 'price', 'category']
    context_object_name = 'product'
    success_url = reverse_lazy('makola:list-products')  # Redirect to product list after successful update

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'makola/product_delete.html'
    context_object_name = 'product'
    message = 'Are you sure you want to delete this product?'
    success_url = reverse_lazy('makola:list-products')  # Redirect to product list after successful deletion
    

class CategoryListView(ListView):
    model = Category
    template_name = 'makola/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'makola/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'makola/category_create.html'
    fields = ['name', 'description']
    context_object_name = 'category'
    success_url = reverse_lazy('makola:list-categories')  # Redirect to category list after successful creation

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'makola/category_update.html'
    fields = ['name', 'description']
    context_object_name = 'category'
    success_url = reverse_lazy('makola:list-categories')  # Redirect to category list after successful update

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'makola/category_delete.html'
    context_object_name = 'category'
    message = 'Are you sure you want to delete this category?'
    success_url = reverse_lazy('makola:list-categories')  # Redirect to category list after successful deletion

