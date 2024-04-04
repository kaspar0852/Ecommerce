from django.urls import path
from .views import CreateAndListOrderView, UpdateDeleteOrderView,UserOrderListView

urlpatterns = [
    path('orders/', CreateAndListOrderView.as_view(), name='order-list-create'),
    path('<int:pk>/', UpdateDeleteOrderView.as_view(), name='order-update-delete'),
    path('user-orders/<int:user_id>/', UserOrderListView.as_view(), name='user-order-list'),
]