from rest_framework import serializers
from .models import Product, ProductImage, ProductType


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        image_data = validated_data.pop('image')  # Extract image data
        product = Product.objects.create(**validated_data)  # Create the product instance

        # Create the product image instance
        ProductImage.objects.create(
            Name=validated_data['Name'],
            Image=image_data.read(),
            Extension=image_data.name.split('.')[-1],
            ProductId=product
        )

        return product


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class GetProductSerializer(serializers.ModelSerializer):
    Product_Type = ProductTypeSerializer(source='ProductTypeId', read_only=True)
    #Product_Image = ProductImageSerializer(source='productimage_set', many=True, read_only=True) #here django searches the releted field and doesnot find it in the productimage model...so it takes the lower case of the model name and ends with _set which can be user here
    Product_Image = ProductImageSerializer(source='image',read_only=True,many=True)#
    class Meta:
        model = Product
        fields = ['id', 'Name', 'Description', 'Expiration_Date', 'UserId','Product_Type','Product_Image']
