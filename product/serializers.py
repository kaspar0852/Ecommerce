from rest_framework import serializers
from .models import Product, ProductImage, ProductType, ProductReview
from customer.models import User


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    user_name = serializers.CharField(source='UserId.Name', read_only=True)
    product_type_name = serializers.CharField(source='ProductTypeId.Name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'Name', 'Description', 'Expiration_Date', 'UserId', 'user_name', 'ProductTypeId',
                  'product_type_name', 'image']
        ref_name = 'ProductProduct'

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

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.UserId = validated_data.get('UserId', instance.UserId)
        instance.ProductTypeId = validated_data.get('ProductTypeId', instance.ProductTypeId)

        image_data = validated_data.get('image')
        if image_data:
            # Update the product image instance
            ProductImage.objects.update_or_create(
                ProductId=instance,
                defaults={
                    'Name': instance.Name,
                    'Image': image_data.read(),
                    'Extension': image_data.name.split('.')[-1]
                }
            )
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Name', 'Age', 'Address']
        ref_name = 'ProductUser'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
        ref_name = 'ProductProductType'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class GetProductSerializer(serializers.ModelSerializer):
    Product_Type = ProductTypeSerializer(source='ProductTypeId', read_only=True)
    # Product_Image = ProductImageSerializer(source='productimage_set', many=True, read_only=True) #here django searches the releted field and doesnot find it in the productimage model...so it takes the lower case of the model name and ends with _set which can be user here
    Product_Image = ProductImageSerializer(source='image', read_only=True, many=True)  #

    class Meta:
        model = Product
        fields = ['id', 'Name', 'Description', 'Expiration_Date', 'UserId', 'Product_Type', 'Product_Image']


class ProductCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()  # Allow input for image field

    class Meta:
        model = Product
        fields = ['id', 'Name', 'Description', 'Expiration_Date', 'UserId', 'ProductTypeId', 'image']


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['Name']


class GetProductReviewSerializer(serializers.ModelSerializer):
    product = ProductNameSerializer(source='ProductId', read_only=True)
    user = UserSerializer(source='UserId', read_only=True)

    class Meta:
        model = ProductReview
        fields = ['id', 'ProductId', 'UserId', 'Rating', 'Review_Text', 'Review_Date', 'product', 'user']
