from django.contrib import admin

# Register your models here.
from .models import Seller,SellerDetails

admin.site.register(Seller)
admin.site.register(SellerDetails)