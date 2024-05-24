from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, LoanViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('customers/<int:pk>/balance/', CustomerViewSet.as_view({'get': 'balance'}), name='customer-balance'),
]

# Esto asegura que el decorador `@action` se registra con un nombre correcto.
CustomerViewSet.balance.url_name = 'customer-balance'