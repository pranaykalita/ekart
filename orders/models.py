from django.db import models

from accounts.models import customerUser
from products.models import Product


# order status

class orderstatus(models.Model):
    status = models.TextField(max_length=50)  # 0 process , 1 confirm, 2 ship, 3 completed/delivered ,4 Rejected , 5 others


# Create your models here.
class Order(models.Model):
    ordernum = models.TextField(max_length=50)
    orderdate = models.DateField(auto_now_add=True)
    ordertime = models.TimeField(auto_now_add=True)
    orderuser = models.ForeignKey(customerUser, on_delete=models.CASCADE, related_name="ordercustomer")
    orderstatus = models.ForeignKey(orderstatus, on_delete=models.CASCADE, related_name='orderstatus')


class orderItm(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='prodordernum')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderproduct')
    quantity = models.IntegerField()
    itmtotal = models.FloatField()
    subtotal = models.FloatField()
    addedon = models.DateTimeField(auto_now_add=True)


class shipAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipordernum')
    country = models.TextField(max_length=150)
    Region = models.TextField(max_length=150)
    Zip = models.TextField(max_length=150)
    Address1 = models.TextField(max_length=150)
    Address2 = models.TextField(max_length=150)
    landmark = models.TextField(max_length=150)
    phone = models.TextField(max_length=150)


class Paymentmode(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='paymntordernum')
    mode = models.TextField(max_length=20)
    paymentOn = models.DateTimeField(auto_now_add=True)
