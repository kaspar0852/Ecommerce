from django.contrib import admin

from product.models import Product,ProductType,ProductImage,ProductReview

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductImage)
admin.site.register(ProductReview)