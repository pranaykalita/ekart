from rest_framework import serializers

from products.models import *


class ProductSrializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDataSrializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'

class CategorySrializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class SubCategorySrializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'