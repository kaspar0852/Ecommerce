from datetime import timezone

from django.db import models
from customer.models import User
from product.models import Product


# Create your models here.

class Wishlist(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    CreatedTime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.CreatedTime = timezone.utc
        super().save(*args, **kwargs)
