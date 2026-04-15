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