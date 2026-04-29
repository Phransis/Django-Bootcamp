from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from makola.models import Category, Product, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView

# Create your views here.

# def homepage(request):
#     products = Product.objects.all()[:8]  # Fetch the first 8 products for display
#     return render(request, 'makola/homepage.html', {'products': products})

class HomepageView(ListView):
    model = Product
    template_name = 'makola/homepage.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Order first, then limit to the first 8 products
        return Product.objects.order_by('-created_at')[:8]

class LoginView(CreateView):
    model = Profile
    template_name = 'makola/login.html'
    fields = ['username', 'password']
    success_url = reverse_lazy('makola:homepage')  # Redirect to homepage after successful login

class LogoutView(LogoutView):
    next_page = reverse_lazy('makola:homepage')

class ProfileListView(ListView):
    model = Profile
    template_name = 'makola/profile_list.html'
    context_object_name = 'profiles'
    paginate_by = 10  # Display 10 profiles per page
    ordering = ['-created_at']  # Order profiles by creation date (newest first)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'makola/profile_detail.html'
    context_object_name = 'profile'

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'makola/profile_create.html'
    fields = ['name', 'username', 'phone_number', 'email', 'password', 'address', 'bio', 'user_type']
    context_object_name = 'profile'
    success_url = reverse_lazy('makola:list-profiles')  # Redirect to profile list after successful creation

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'makola/profile_edit.html'
    fields = ['name', 'phone_number', 'address', 'bio', 'user_type']
    context_object_name = 'profile'
    success_url = reverse_lazy('makola:list-profiles')  # Redirect to profile list after successful update

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'makola/profile_delete.html'
    context_object_name = 'profile'
    message = 'Are you sure you want to delete this profile?'
    success_url = reverse_lazy('makola:list-profiles')  # Redirect to profile list after successful deletion

class ProductListView(ListView):
    model = Product
    template_name = 'makola/product_list.html'
    context_object_name = 'products'
    paginate_by = 10  # Display 10 products per page
    queryset = Product.objects.select_related('category')  # Use select_related to optimize database queries by fetching related category data in a single query
    ordering = ['-created_at']  # Order products by creation date (newest first)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'makola/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'makola/product_create.html'
    fields = ['name', 'description', 'price', 'category', 'image']
    context_object_name = 'product'
    success_url = reverse_lazy('makola:list-products')  # Redirect to product list after successful creation

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'makola/product_update.html'
    fields = ['name', 'description', 'price', 'category', 'image']
    context_object_name = 'product'
    success_url = reverse_lazy('makola:list-products')  # Redirect to product list after successful update

class ProductDeleteView(LoginRequiredMixin, DeleteView):
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

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'makola/category_create.html'
    fields = ['name', 'description']
    context_object_name = 'category'
    success_url = reverse_lazy('makola:list-categories')  # Redirect to category list after successful creation

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'makola/category_update.html'
    fields = ['name', 'description']
    context_object_name = 'category'
    success_url = reverse_lazy('makola:list-categories')  # Redirect to category list after successful update

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'makola/category_delete.html'
    context_object_name = 'category'
    message = 'Are you sure you want to delete this category?'
    success_url = reverse_lazy('makola:list-categories')  # Redirect to category list after successful deletion

