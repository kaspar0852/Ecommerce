from django.db.models import Max
from django.shortcuts import render
from rest_framework import viewsets, generics, status, views
from .serializers import UserFullSerializer, UserSerializerWithoutOrderNumber
from .models import User
from rest_framework.response import Response
from .dtos import UserDTO
from .pagination import LargeResultsPagination


# Create your views here.

class CreateCustomerViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    pagination_class = LargeResultsPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserFullSerializer
        return UserSerializerWithoutOrderNumber

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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        dto_data = {
            'Name': instance.Name,
            'Age': instance.Age,
            'Address': instance.Address,
            'Phone': instance.Phone,
            'IsActive': instance.IsActive,
            'OrderNumber': instance.OrderNumber,
        }
        response_data = UserDTO(data=dto_data)
        print(response_data)
        response_data.is_valid()
        response_data = response_data.data

        print(response_data)
        # Return the response
        return Response(dto_data, status=status.HTTP_201_CREATED)


class UpdateAndDeleteCustomerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    pagination_class = LargeResultsPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserFullSerializer
        return UserSerializerWithoutOrderNumber


