from rest_framework import serializers
from products.models import *
from accounts.models import accountUser


# SubcategorySerializer
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['subcatgName']

#Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryName']

# List Category With SubCategory
class CategorySubcategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['categoryName', 'subcategories']

# product Details
class ProductdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['about', 'description', 'SKU']

# product Details
class ProductSerializer(serializers.ModelSerializer):
    product = ProductdetailSerializer()
    category = CategorySerializer()
    subCategory = SubcategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'item', 'price', 'quantity', 'category', 'subCategory','product', 'image']


# Lsit username And Email of Registered User

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountUser
        fields = ['username', 'email']


