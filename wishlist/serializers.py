from rest_framework import serializers
from customer.models import User
from product.models import Product
from wishlist.models import Wishlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Name', 'Age']
        ref_name = 'WishlistUser'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['Name']
        ref_name = 'WishlistProduct'


class WishlistSerializer(serializers.ModelSerializer):
    CreatedTime = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id','UserId', 'ProductId', 'CreatedTime']


class GetWishListSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='UserId',read_only=True)
    product = ProductSerializer(source='ProductId',read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id','UserId', 'user', 'ProductId', 'product', 'CreatedTime']
