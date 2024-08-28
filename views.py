
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Bank, Customer
from .serializers import BankSerializer, CustomerSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepositView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data.get('amount')
        if amount is not None:
            customer = request.user
            customer.balance += float(amount)
            customer.save()
            return Response({'message': 'Deposit successful', 'balance': customer.balance})
        return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

class WithdrawalView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data.get('amount')
        customer = request.user
        if amount is not None and customer.balance >= float(amount):
            customer.balance -= float(amount)
            customer.save()
            return Response({'message': 'Withdrawal successful', 'balance': customer.balance})
        return Response({'error': 'Invalid amount or insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

urlpatterns = [
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]