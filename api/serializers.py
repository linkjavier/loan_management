from rest_framework import serializers
from .models import Customer, Loan, Payment, PaymentLoanDetail

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentLoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentLoanDetail
        fields = '__all__'
