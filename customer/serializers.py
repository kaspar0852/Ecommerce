from rest_framework import serializers
from .models import User


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerWithoutOrderNumber(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Name', 'Age', 'Address', 'Phone', 'IsActive')
