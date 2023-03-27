from django.contrib import admin

# Register your models here.
from .models import Category,SubCategory,Product,ProductDetail

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'quantity','image')
@admin.register(ProductDetail)
class Admin(admin.ModelAdmin):
    list_display = ('product','about')

admin.site.register(Category)
admin.site.register(SubCategory)