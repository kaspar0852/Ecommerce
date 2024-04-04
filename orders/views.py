from django.shortcuts import render
from rest_framework import generics, filters
from .pagination import LargeResultsPagination

from orders.models import Order
from .serializers import OrderSerializer, GetOrderListSerializer


# Create your views here.

class CreateAndListOrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    pagination_class = LargeResultsPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['OrderSlug']
    ordering_fields = ['NumberOfOrders']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_filter = self.request.query_params.get('search')
        ordering_filter = self.request.query_params.get('ordering')
        print(search_filter)

        if search_filter:
            queryset = queryset.filter(OrderSlug__icontains=search_filter)

        if ordering_filter:
            queryset = queryset.order_by(ordering_filter)

        if self.request.GET.get('page'):
            self.paginate_queryset(queryset)

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetOrderListSerializer
        return OrderSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class UpdateDeleteOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserOrderListView(generics.ListAPIView):
    serializer_class = GetOrderListSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Order.objects.filter(UserId=user_id)
