from rest_framework import serializers
from products.models import *


class SubcategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	SubCategory = SubcategorySerializer()
	class Meta:
		model = Category
		fields = '__all__'

class productDetailserialiizer(serializers.ModelSerializer):
	class Meta:
		model = ProductDetail
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	productdetail = productDetailserialiizer()
	class Meta:
		model = Product
		fields = '__all__'
		