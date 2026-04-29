from django.urls import path
from . import views

app_name = 'makola'
urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/list/', views.ProfileListView.as_view(), name='list-profiles'), 
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/create/', views.ProfileCreateView.as_view(), name='create-profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='update-profile'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),

    
    path('buyer/dashboard/', views.BuyerDashboardView.as_view(), name='buyer-dashboard'),
    path('seller/dashboard/', views.SellerDashboardView.as_view(), name='seller-dashboard'),

    path('product/list/', views.ProductListView.as_view(), name='list-products'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='create-product'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='update-product'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete-product'),

    path('category/list/', views.CategoryListView.as_view(), name='list-categories'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='create-category'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='update-category'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='delete-category'),
]