from django.shortcuts import render
from rest_framework import generics
from api.serializers import *
from products.models import *


class productApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSrializer

class productDataApiView(generics.ListCreateAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDataSrializer


class CategoryApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySrializer


class SubCategoryApiView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySrializer