from django.urls import path
from .views import ProductCreateListView, ProductListView, ProductUpdateView

urlpatterns = [
    path('create/', ProductCreateListView.as_view(), name='product-list-create'),
    path('list/', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductUpdateView.as_view(), name='product-update')
]
