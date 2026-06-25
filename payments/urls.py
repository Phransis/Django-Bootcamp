from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.PaymentAPIView.as_view(), name='payments'),
    path('success/', views.PaymentAPIView.as_view(), name='payment_success'),
]