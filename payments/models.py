import uuid

from django.db import models

# Create your models here.

class Payment(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Successful'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('momo', 'Momo'),
        ('cash', 'Cash'),
        ('crypto', 'Crypto'),
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')

    def __str__(self):
        return f'Payment of ${self.amount} at {self.timestamp}'