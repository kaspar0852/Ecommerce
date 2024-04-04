from tkinter import Image

from django.db import models
from customer.models import User


# Create your models here.


class ProductType(models.Model):
    Name = models.CharField(max_length=250)
    Description = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=250)
    Description = models.TextField(max_length=250)
    Expiration_Date = models.DateField()
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    ProductTypeId = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class ProductImage(models.Model):
    Name = models.CharField(max_length=250)
    Image = models.BinaryField()
    Extension = models.CharField(max_length=20)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')

    # here a related name is defined so i can use this in the serializer to show relation with product

    def __str__(self):
        return self.Name


class ProductReview(models.Model):
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    Rating = models.IntegerField()
    Review_Text = models.TextField()
    Review_Date = models.DateField()

    def __str__(self):
        return self.Rating
