from rest_framework import serializers
from .models import Customer, Loan, Payment, PaymentLoanDetail

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Customer.

    Este serializer convierte las instancias del modelo Customer en formatos
    como JSON, y viceversa, permitiendo la validación y deserialización de
    los datos del cliente.

    Meta:
        model (Customer): El modelo que será serializado.
        fields (str): Todos los campos del modelo serán incluidos.
    """
    class Meta:
        model = Customer
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Loan.

    Este serializer convierte las instancias del modelo Loan en formatos
    como JSON, y viceversa, permitiendo la validación y deserialización de
    los datos del préstamo.

    Meta:
        model (Loan): El modelo que será serializado.
        fields (str): Todos los campos del modelo serán incluidos.
    """
    class Meta:
        model = Loan
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Payment.

    Este serializer convierte las instancias del modelo Payment en formatos
    como JSON, y viceversa, permitiendo la validación y deserialización de
    los datos del pago.

    Meta:
        model (Payment): El modelo que será serializado.
        fields (str): Todos los campos del modelo serán incluidos.
    """
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentLoanDetailSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo PaymentLoanDetail.

    Este serializer convierte las instancias del modelo PaymentLoanDetail en formatos
    como JSON, y viceversa, permitiendo la validación y deserialización de
    los datos del detalle del pago asociado con un préstamo específico.

    Meta:
        model (PaymentLoanDetail): El modelo que será serializado.
        fields (str): Todos los campos del modelo serán incluidos.
    """
    class Meta:
        model = PaymentLoanDetail
        fields = '__all__'

class CustomerBalanceSerializer(serializers.ModelSerializer):
    available_amount = serializers.SerializerMethodField()
    total_debt = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['external_id', 'score', 'available_amount', 'total_debt']

    def get_available_amount(self, obj):
        total_debt = self.get_total_debt(obj)
        return obj.score - total_debt

    def get_total_debt(self, obj):
        loans = Loan.objects.filter(customer=obj, status__in=[1, 2])  # Pending or Active
        return sum([loan.outstanding for loan in loans])

