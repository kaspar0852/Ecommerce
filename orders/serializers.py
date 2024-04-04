from customer import serializers
from .models import Order, OrderStatus
from customer.models import User
from product.models import Product, ProductType
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Name', 'Age']
        ref_name = 'OrderUser'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['Name']
        ref_name = 'OrderProductType'


class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer(source='ProductTypeId', read_only=True)

    class Meta:
        model = Product
        fields = ['Name', 'product_type']
        ref_name = 'OrderProduct'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    OrderSlug = serializers.UUIDField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'OrderStatusId', 'ProductId', 'UserId',
                  'NumberOfOrders', 'OrderSlug', 'Is_Confirmed']


class GetOrderListSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='UserId', read_only=True)
    product = ProductSerializer(source='ProductId', read_only=True)
    order_status = OrderStatusSerializer(source='OrderStatusId', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_status', 'ProductId', 'UserId',
                  'NumberOfOrders', 'OrderSlug', 'Is_Confirmed', 'user', 'product']
