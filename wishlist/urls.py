from django.urls import path

from .views import CreateAndGetWishListView, UpdateDeleteWishListView, GetUserWishListView

urlpatterns = [
    path('create/', CreateAndGetWishListView.as_view(), name='wishlist-create-get'),
    path('<int:pk>/', UpdateDeleteWishListView.as_view(), name='wishlist-update-delete'),
    path('user-wishlists/<int:user_id>/', GetUserWishListView.as_view(), name='user-wishlist-list'),
]