from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from  rest_framework.mixins import RetrieveModelMixin,ListModelMixin

from products.models import *
from .serializers import *

class ProductApiview(ListModelMixin,GenericAPIView):
	queryset = Product.objects.select_related('productdetail','category','subCategory').all()
	serializer_class = ProductSerializer
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

class ProductsRetriveApiview(GenericAPIView,RetrieveModelMixin):
	queryset = Product.objects.select_related('productdetail','category','subCategory').all()
	serializer_class = ProductSerializer
	lookup_field = 'id'
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)



class CategoryApiview(ListModelMixin,GenericAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	def get(self, request,*args,**kwargs):
		return self.list(request,*args, **kwargs)

