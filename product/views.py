from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, GetProductSerializer


# Create your views here.


class ProductCreateListView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
