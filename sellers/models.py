from django.db import models

# Create your models here.

# seller
class Seller(models.Model):
    username = models.CharField(max_length=50)
    sellerEmail = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username    

class SellerDetails(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    countrycode = models.CharField(max_length=4)
    phone = models.CharField(max_length=12)
    profileImg = models.ImageField(upload_to="media/seller_prof", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    


