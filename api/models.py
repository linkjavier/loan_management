from django.db import models

# Customer Model
class Customer(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1)

    def __str__(self):
        return self.external_id
    
# Loan Model
class Loan(models.Model):
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
        return self.external_id
    
# Payment Model
class Payment(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=[
        (1, 'Completed'), (2, 'Rejected')
    ], default=1)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.external_id
    
# PaymentLoanDetail
class PaymentLoanDetail(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.payment.external_id} - {self.loan.external_id}"
