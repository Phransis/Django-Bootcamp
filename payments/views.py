from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payments.models import Payment
from payments.serializers import PaymentSerializer

class PaymentAPIView(APIView):

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        payments = Payment.objects.order_by('-timestamp')
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    