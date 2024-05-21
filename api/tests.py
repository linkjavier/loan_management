from django.test import TestCase
from .models import Customer, Loan, Payment

class CustomerTestCase(TestCase):
    """
    TestCase para el modelo Customer.

    Este conjunto de pruebas verifica la correcta creación y persistencia de los datos
    del modelo Customer en la base de datos de prueba.
    """
    def setUp(self):
        """
        Configuración inicial para las pruebas de Customer.

        Se ejecuta antes de cada prueba, creando una instancia de Customer para su uso en las pruebas.
        """
        Customer.objects.create(external_id="customer_01", score=1000.0, status=1)

    def test_customer_creation(self):
        """
        Prueba la creación de un Customer.

        Verifica que el Customer creado en setUp tiene los atributos correctos.
        """
        customer = Customer.objects.get(external_id="customer_01")
        self.assertEqual(customer.score, 1000.0)
        self.assertEqual(customer.status, 1)

class LoanTestCase(TestCase):
    """
    TestCase para el modelo Loan.

    Este conjunto de pruebas verifica la correcta creación y persistencia de los datos
    del modelo Loan en la base de datos de prueba.
    """
    def setUp(self):
        """
        Configuración inicial para las pruebas de Loan.

        Se ejecuta antes de cada prueba, creando una instancia de Customer y Loan para su uso en las pruebas.
        """
        customer = Customer.objects.create(external_id="customer_02", score=2000.0, status=1)
        Loan.objects.create(external_id="loan_01", customer=customer, amount=500.0, outstanding=500.0, status=2)

    def test_loan_creation(self):
        """
        Prueba la creación de un Loan.

        Verifica que el Loan creado en setUp tiene los atributos correctos.
        """
        loan = Loan.objects.get(external_id="loan_01")
        self.assertEqual(loan.amount, 500.0)
        self.assertEqual(loan.outstanding, 500.0)
        self.assertEqual(loan.status, 2)

class PaymentTestCase(TestCase):
    """
    TestCase para el modelo Payment.

    Este conjunto de pruebas verifica la correcta creación y persistencia de los datos
    del modelo Payment en la base de datos de prueba.
    """
    def setUp(self):
        """
        Configuración inicial para las pruebas de Payment.

        Se ejecuta antes de cada prueba, creando instancias de Customer, Loan y Payment para su uso en las pruebas.
        """
        customer = Customer.objects.create(external_id="customer_03", score=3000.0, status=1)
        loan = Loan.objects.create(external_id="loan_02", customer=customer, amount=1000.0, outstanding=1000.0, status=2)
        Payment.objects.create(external_id="payment_01", customer=customer, total_amount=500.0, status=1)

    def test_payment_creation(self):
        """
        Prueba la creación de un Payment.

        Verifica que el Payment creado en setUp tiene los atributos correctos.
        """
        payment = Payment.objects.get(external_id="payment_01")
        self.assertEqual(payment.total_amount, 500.0)
        self.assertEqual(payment.status, 1)
