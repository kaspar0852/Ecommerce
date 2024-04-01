from django.db.models import Max
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import UserFullSerializer, UserSerializerWithoutOrderNumber
from .models import User
from rest_framework.response import Response


# Create your views here.

class CreateCustomerViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserFullSerializer
        return UserSerializerWithoutOrderNumber

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateAndDeleteCustomerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserFullSerializer
