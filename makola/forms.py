from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'username',
            'phone_number',
            'email',
            'address',
            'bio',
            'user_type',
        ]
        field_order = [
            'name',
            'username',
            'phone_number',
            'email',
            'address',
            'bio',
            'user_type',
            'password1',
            'password2',
        ]
