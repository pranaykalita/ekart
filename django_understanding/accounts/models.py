from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class accountData(models.Model):

    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    userphone = models.IntegerField()
    
    addressfield1 = models.CharField( max_length=100)
    addressfield2 = models.CharField( max_length=100)
    country = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    pincode = models.IntegerField()
