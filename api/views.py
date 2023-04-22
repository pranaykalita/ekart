from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from  rest_framework.mixins import RetrieveModelMixin,ListModelMixin

from products.models import *
from .serializers import *

# show all products
class ProductApiview(ListModelMixin,GenericAPIView):
	queryset = Product.objects.select_related('productdetail','category','subCategory').all()
	serializer_class = ProductSerializer
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

#Products Single by id
class ProductsRetriveApiview(GenericAPIView,RetrieveModelMixin):
	queryset = Product.objects.select_related('productdetail','category','subCategory').all()
	serializer_class = ProductSerializer
	lookup_field = 'id'
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

# product by category
class ProductbyCategoryApiview(ListModelMixin,GenericAPIView):
	serializer_class = ProductSerializer
	def get_queryset(self):
		queryset = Product.objects.all()
		category_name = self.request.query_params.get('categoryName',None)
		subcategory_name = self.request.query_params.get('subcatgName',None)
		if category_name is not None:
			queryset = queryset.filter(category__categoryName=category_name)
		if subcategory_name is not None:
			queryset = queryset.filter(subCategory__subcatgName=subcategory_name)
		return queryset
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

# show categoryAPI with subctegory
class CategoryApiview(ListModelMixin,GenericAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	def get(self, request,*args,**kwargs):
		return self.list(request,*args, **kwargs)

