from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, GetProductSerializer, ProductCreateSerializer
from django.shortcuts import get_object_or_404
from .pagination import LargeResultsPagination


# Create your views here.

class ProductCreateListView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = GetProductSerializer
    pagination_class = LargeResultsPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('page'):
            page = self.paginate_queryset(queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        # print(serializer.data['Name'])

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
