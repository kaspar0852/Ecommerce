from django.urls import path
from .views import (ProductCreateListView,
                    ProductListView, ProductUpdateView,
                    ProductReviewCreateView,ProductReviewUpdateView)

urlpatterns = [
    path('create/', ProductCreateListView.as_view(), name='product-list-create'),
    path('list/', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('review/', ProductReviewCreateView.as_view(), name='product-review-create'),
    path('review/<int:pk>/', ProductReviewUpdateView.as_view(), name='product-review-update'),
]
