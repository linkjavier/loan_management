# loan_management

API using Django Rest Framework to manage and monitor customer loans and payments

# Descripción General:

# MODELOS
Customer Model
- external_id: Un identificador único para el cliente, usado externamente.
- score: El puntaje del cliente, que podría determinar la elegibilidad para préstamos.
- status: El estado del cliente, con opciones 'Active' (1) y 'Inactive' (2).

Loan Model
- external_id: Un identificador único para el préstamo.
- customer: Una relación con el cliente que tomó el préstamo.
- amount: El monto total del préstamo.
- outstanding: El monto pendiente de pago del préstamo.
- status: El estado del préstamo, con opciones 'Pending' (1), 'Active' (2), 'Rejected' (3) y 'Paid' (4).
- contract_version: La versión del contrato asociada al préstamo.
- taken_at: La fecha y hora en que se tomó el préstamo.

Payment Model
- external_id: Un identificador único para el pago.
- customer: Una relación con el cliente que realizó el pago.
- total_amount: El monto total del pago.
- status: El estado del pago, con opciones 'Completed' (1) y 'Rejected' (2).
- payment_date: La fecha y hora en que se realizó el pago, se asigna automáticamente al crearse.

PaymentLoanDetail Model
- payment: Una relación con el pago.
- loan: Una relación con el préstamo.
- amount: El monto del pago que se aplicó a este préstamo específico.

Nota: Cada modelo incluye un método __str__ para retornar una representación legible y útil del objeto, facilitando la identificación de instancias en la interfaz de administración y en el shell de Django.

=========================================================

# HOW TO USE

To acces to Djando Manager you need to create a super user
python manage.py createsuperuser

Username: mo_user
Email: javiercharria@gmail.com
Password: mo_password

If we need to make changes to the models it is necessary to run in bash: 
$ python manage.py makemigrations
$ python manage.py migrate

The project can be used, both locally and Dockerized.
It is recommended to use Docker Compose to run in different environments without major problems.


# DOCKERIZED SECTION

1. Verify your Docker and Docker Compose installation
2. Run via console $ docker compose build
3. Verify a good construction of the Build and run $ docker compose up
4. Voila! You can now access the server on port 8000 (ex.: http://localhost:8000/api/customers/)

# Create a Super User
If you need to access the Django admin interface, create a superuser by running:
$ docker compose run web python manage.py createsuperuser

====================================================

# Automatic Tests
To run your automated tests inside the container, use the following command: 
$ docker compose run web python manage.py test

Esta documentación ayuda a entender la finalidad y el uso de cada test case, así como la configuración específica y las verificaciones realizadas en cada prueba.

# CustomerTestCase

 Descripción: Verifica la correcta creación y persistencia de los datos del modelo Customer.
- setUp:Crea una instancia de Customer con external_id="customer_01", score=1000.0 y status=1 antes de cada prueba.
- test_customer_creation: Verifica que la instancia de Customer creada en setUp tiene los atributos score y status correctos.

# LoanTestCase

 Descripción: Verifica la correcta creación y persistencia de los datos del modelo Loan.
- setUp: Crea una instancia de Customer y una instancia de Loan asociada a ese Customer antes de cada prueba.
- test_loan_creation: Verifica que la instancia de Loan creada en setUp tiene los atributos amount, outstanding y status correctos.

# PaymentTestCase

 Descripción: Verifica la correcta creación y persistencia de los datos del modelo Payment.
- setUp: Crea instancias de Customer, Loan y Payment asociadas antes de cada prueba.
- test_payment_creation: Verifica que la instancia de Payment creada en setUp tiene los atributos total_amount y status correctos.

# Funcionalidad de los Tests:

- Configuración Inicial (setUp): Cada test case configura los datos necesarios antes de ejecutar cada prueba. Esto asegura que cada prueba tenga un estado inicial conocido.

- Pruebas de Atributos: Cada prueba verifica que los atributos de las instancias creadas son correctos, asegurando que los modelos se crean y se guardan adecuadamente en la base de datos.

- Aislamiento: Cada prueba se ejecuta en un entorno de base de datos separado y controlado, lo que garantiza que las pruebas no se afecten entre sí.



By Javier Charria