from rest_framework import serializers
from products.models import *


class SubcategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ['subcatgName']

class CategorySerializer(serializers.ModelSerializer):
	# subcategory = SubcategorySerializer()
	class Meta:
		model = Category
		fields = '__all__'

class productDetailserialiizer(serializers.ModelSerializer):
	class Meta:
		model = ProductDetail
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	productdetail = productDetailserialiizer()
	category = CategorySerializer()
	subCategory = SubcategorySerializer()
	class Meta:
		model = Product
		fields = '__all__'
		