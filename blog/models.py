from django.db import models

# Create your models here.


class Author(models.Model):
    CATEGORY_CHOICES = [
        ('TECHNOLOGY', 'Technology'),
        ('LIFESTYLE', 'Lifestyle'),
        ('TRAVEL', 'Travel'),
        ('FOOD', 'Food'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='TECHNOLOGY')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('TECHNOLOGY', 'Technology'),
        ('LIFESTYLE', 'Lifestyle'),
        ('TRAVEL', 'Travel'),
        ('FOOD', 'Food'),
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='TECHNOLOGY')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

