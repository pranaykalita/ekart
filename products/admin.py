from django.contrib import admin

# Register your models here.
from .models import Category,SubCategory,Products,ProductDetails,Review

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Products)
admin.site.register(ProductDetails)
admin.site.register(Review)
