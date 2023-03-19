from django.db import models

# Create your models here.

# User DataModel

class ek_user(models.Model):
    print("abc")

# profile
class ek_users_profile(models.Model):
    id = models.IntegerField(primary_key=True),
    user_id = models.ForeignKey(ek_user, on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    sex = models.CharField(max_length = 12)
    countrycode = models.IntegerField()
    phone = models.IntegerField()
    profile_image = models.URLField(max_length = 200)

# shippng address
class ek_shippingaddress(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(ek_user, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 150)
    address1 = models.CharField(max_length = 150)
    address2 = models.CharField(max_length = 150)
    landmark = models.CharField(max_length = 150)
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    pincode = models.IntegerField()

# billingaddress
class ek_billingaddress(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(ek_user, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 150)
    address1 = models.CharField(max_length = 150)
    address2 = models.CharField(max_length = 150)
    landmark = models.CharField(max_length = 150)
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    pincode = models.IntegerField()
    
    
    
    
    
    