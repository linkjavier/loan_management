# loan_management

API using Django Rest Framework to manage and monitor customer loans and payments

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


# Automatic Tests
To run your automated tests inside the container, use the following command: 
$ docker compose run web python manage.py test


# Create a Super User
If you need to access the Django admin interface, create a superuser by running:
$ docker compose run web python manage.py createsuperuser


By Javier Charria