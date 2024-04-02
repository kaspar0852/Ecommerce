from typing import Any
from django.db import models
from django.db.models import Max


# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=250)
    Age = models.IntegerField(null=False, blank=False)
    Address = models.CharField(max_length=250, null=False, blank=False)
    Phone = models.IntegerField(null=False)
    IsActive = models.BooleanField(default=True)
    OrderNumber = models.IntegerField(null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            max_order_number = User.objects.aggregate(Max('OrderNumber'))['OrderNumber__max']

            if max_order_number is not None:
                self.OrderNumber = max_order_number + 1
            else:
                self.OrderNumber = 1

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.Name

        #return f"Name: {self.Name}, Age: {self.Age}, Address: {self.Address}, Phone: {self.Phone}, IsActive: {self.IsActive}, OrderNumber: {self.OrderNumber}"
