from django.contrib import admin

# Register your models here.
from .models import ecom_seller,ecom_seller_details

admin.site.register(ecom_seller)
admin.site.register(ecom_seller_details)