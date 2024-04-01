from rest_framework import serializers


class UserDTO(serializers.Serializer):
    Name = serializers.CharField()
    Age = serializers.IntegerField()
    Address = serializers.CharField()
    Phone = serializers.CharField()
    IsActive = serializers.BooleanField()
    OrderNumber = serializers.CharField()
