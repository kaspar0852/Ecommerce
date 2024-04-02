from django.urls import path
from .views import ProductCreateListView,ProductListView


urlpatterns = [
    path('create/', ProductCreateListView.as_view(), name='product-list-create'),
    path('list/', ProductListView.as_view(), name='product-list'),
]
