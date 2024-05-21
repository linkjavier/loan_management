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
