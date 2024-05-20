from django.test import TestCase
from .models import Customer, Loan, Payment

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(external_id="customer_01", score=1000.0, status=1)

    def test_customer_creation(self):
        customer = Customer.objects.get(external_id="customer_01")
        self.assertEqual(customer.score, 1000.0)
        self.assertEqual(customer.status, 1)

class LoanTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(external_id="customer_02", score=2000.0, status=1)
        Loan.objects.create(external_id="loan_01", customer=customer, amount=500.0, outstanding=500.0, status=2)

    def test_loan_creation(self):
        loan = Loan.objects.get(external_id="loan_01")
        self.assertEqual(loan.amount, 500.0)
        self.assertEqual(loan.outstanding, 500.0)
        self.assertEqual(loan.status, 2)

class PaymentTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(external_id="customer_03", score=3000.0, status=1)
        loan = Loan.objects.create(external_id="loan_02", customer=customer, amount=1000.0, outstanding=1000.0, status=2)
        Payment.objects.create(external_id="payment_01", customer=customer, total_amount=500.0, status=1)

    def test_payment_creation(self):
        payment = Payment.objects.get(external_id="payment_01")
        self.assertEqual(payment.total_amount, 500.0)
        self.assertEqual(payment.status, 1)
