from django.urls import path
from . import views

app_name = 'makola'
urlpatterns = [
    path('', views.homepage, name='homepage')
]