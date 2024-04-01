from django.urls import path
from .views import CreateCustomerViewSet,UpdateAndDeleteCustomerView


urlpatterns = [
    path('customers/', CreateCustomerViewSet.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', UpdateAndDeleteCustomerView.as_view(), name='customer-detail'),
]
