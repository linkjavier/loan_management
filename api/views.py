from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Customer, Loan, Payment, PaymentLoanDetail
from .serializers import CustomerSerializer, LoanSerializer, PaymentSerializer, PaymentLoanDetailSerializer, CustomerBalanceSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        request.data['status'] = 1  # Status 'Active'
        return super().create(request, *args, **kwargs)
    
    @action(detail=True, methods=['get'])
    def balance(self, request, pk=None):
        customer = self.get_object()
        serializer = CustomerBalanceSerializer(customer)
        return Response(serializer.data)

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        customer_external_id = request.data.get('customer_external_id')
        try:
            customer = Customer.objects.get(external_id=customer_external_id)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        if customer.score >= float(request.data['amount']):
            request.data['status'] = 2  # Status 'Active'
            request.data['outstanding'] = request.data['amount']
            request.data['customer'] = customer.id  # Set customer ID in the request data
            return super().create(request, *args, **kwargs)
        else:
            return Response({"error": "Loan amount exceeds customer's score"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        customer_external_id = request.query_params.get('customer_external_id')
        if customer_external_id:
            self.queryset = self.queryset.filter(customer__external_id=customer_external_id)
        return super().list(request, *args, **kwargs)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        customer = Customer.objects.get(external_id=request.data['customer'])
        loans = Loan.objects.filter(customer=customer, status=2)  # Active loans
        total_debt = sum([loan.outstanding for loan in loans])

        if total_debt < float(request.data['total_amount']):
            return Response({"error": "Payment exceeds total debt"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment = super().create(request, *args, **kwargs)
        for loan in loans:
            if loan.outstanding > 0:
                payment_amount = min(loan.outstanding, float(request.data['total_amount']))
                PaymentLoanDetail.objects.create(payment=payment, loan=loan, amount=payment_amount)
                loan.outstanding -= payment_amount
                if loan.outstanding == 0:
                    loan.status = 4  # Status 'Paid'
                loan.save()
                request.data['total_amount'] -= payment_amount
                if request.data['total_amount'] <= 0:
                    break

        return payment

