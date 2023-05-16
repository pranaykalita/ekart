import uuid
from django.db import models
from products.models import Product
from accounts.models import customerUser


# Create your models here.

# cart
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    customeruser = models.OneToOneField(customerUser, on_delete=models.CASCADE, related_name='cartcustomer')
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True,
                       related_name='cartitems')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cart)
