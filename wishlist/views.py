from django.shortcuts import render
from rest_framework import generics, filters
from .models import Wishlist
from .serializers import WishlistSerializer, GetWishListSerializer
from .pagination import LargeResultsPagination


class CreateAndGetWishListView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    pagination_class = LargeResultsPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetWishListSerializer
        return WishlistSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.GET.get('page'):
            self.paginate_queryset(queryset)

        return queryset


class UpdateDeleteWishListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetWishListSerializer
        return WishlistSerializer


class GetUserWishListView(generics.ListAPIView):
    serializer_class = GetWishListSerializer
    pagination_class = LargeResultsPagination

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')

        queryset = Wishlist.objects.filter(UserId=user_id)

        if self.request.GET.get('page'):
            self.paginate_queryset(queryset)

        return queryset
