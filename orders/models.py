import uuid
from django.db import models
from customer.models import User
from product.models import Product


class OrderStatus(models.Model):
    SystemName = models.CharField(max_length=250)
    DisplayName = models.CharField(max_length=250)

    def __str__(self):
        return self.DisplayName


class Order(models.Model):
    OrderStatusId = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    NumberOfOrders = models.IntegerField()
    OrderSlug = models.UUIDField()
    Is_Confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.OrderSlug = uuid.uuid4()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.OrderSlug
