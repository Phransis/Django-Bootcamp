from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView

from payments.models import Payment


# Create your views here.

class PaymentView(CreateView):
    model = Payment
    fields = ['amount']
    # template_name = 'payments/payment_form.html'

    # def form_valid(self, form):
    #     return JsonResponse({'message': 'Payment processed successfully'})


def payment_success(request):
    return JsonResponse({'message': 'Payment processed successfully'})