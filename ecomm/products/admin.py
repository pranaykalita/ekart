from django.contrib import admin

# Register your models here.
from .models import ecom_category,ecom_subcategory,ecom_products,ecom_productDetails,ecom_review

admin.site.register(ecom_category)
admin.site.register(ecom_subcategory)
admin.site.register(ecom_products)
admin.site.register(ecom_productDetails)
admin.site.register(ecom_review)
