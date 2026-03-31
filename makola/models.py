from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(AbstractUser):

    USER_TYPES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True, default='User')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField()
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user_type}"
    