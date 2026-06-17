from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.PaymentView.as_view(), name='payments'),
    path('success/', views.payment_success, name='payment_success'),
]