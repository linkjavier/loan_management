from django.db import models

# Customer Model
class Customer(models.Model):
    """
    Modelo que representa a un cliente.

    Attributes:
        external_id (str): ID externo único del cliente.
        score (Decimal): Puntaje del cliente que puede usarse para determinar la elegibilidad para un préstamo.
        status (int): Estado del cliente, donde 1 es 'Active' y 2 es 'Inactive'.
    """
    external_id = models.CharField(max_length=100, unique=True)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1)

    def __str__(self):
        """
        Representa el modelo Customer como una cadena.

        Returns:
            str: El ID externo del cliente.
        """
        return self.external_id
    
# Loan Model
class Loan(models.Model):
    """
    Modelo que representa un préstamo.

    Attributes:
        external_id (str): ID externo único del préstamo.
        customer (ForeignKey): Relación con el cliente que tomó el préstamo.
        amount (Decimal): Monto total del préstamo.
        outstanding (Decimal): Monto pendiente del préstamo.
        status (int): Estado del préstamo, donde 1 es 'Pending', 2 es 'Active', 3 es 'Rejected', y 4 es 'Paid'.
        contract_version (str): Versión del contrato asociado con el préstamo.
        taken_at (datetime): Fecha y hora en que se tomó el préstamo.
    """
    external_id = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    outstanding = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=[
        (1, 'Pending'), (2, 'Active'), (3, 'Rejected'), (4, 'Paid')
    ], default=1)
    contract_version = models.CharField(max_length=100, null=True, blank=True)
    taken_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        Representa el modelo Loan como una cadena.

        Returns:
            str: El ID externo del préstamo.
        """
        return self.external_id
    
# Payment Model
class Payment(models.Model):
    """
    Modelo que representa un pago realizado por un cliente.

    Attributes:
        external_id (str): ID externo único del pago.
        customer (ForeignKey): Relación con el cliente que realizó el pago.
        total_amount (Decimal): Monto total del pago.
        status (int): Estado del pago, donde 1 es 'Completed' y 2 es 'Rejected'.
        payment_date (datetime): Fecha y hora en que se realizó el pago.
    """
    external_id = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=[
        (1, 'Completed'), (2, 'Rejected')
    ], default=1)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Representa el modelo Payment como una cadena.

        Returns:
            str: El ID externo del pago.
        """
        return self.external_id
    
# PaymentLoanDetail
class PaymentLoanDetail(models.Model):
    """
    Modelo que representa los detalles del pago asociados con un préstamo específico.

    Attributes:
        payment (ForeignKey): Relación con el pago.
        loan (ForeignKey): Relación con el préstamo.
        amount (Decimal): Monto del pago aplicado a este préstamo específico.
    """
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Representa el modelo PaymentLoanDetail como una cadena.

        Returns:
            str: Una cadena que combina el ID externo del pago y el ID externo del préstamo.
        """
        return f"{self.payment.external_id} - {self.loan.external_id}"
