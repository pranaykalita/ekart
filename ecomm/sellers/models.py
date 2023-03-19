from django.db import models

# Create your models here.

# seller
class ecom_seller(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    seller_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username    

class ecom_seller_details(models.Model):
    seller_id = models.ForeignKey(ecom_seller, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    countrycode = models.CharField(max_length=4)
    phone = models.CharField(max_length=12)
    profile_img = models.ImageField(upload_to="media/seller_prof", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    


