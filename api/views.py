from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import permissions
from products.models import Product
from .serializer import ProductSerializer


# Create your views here.
class ProductListView(viewsets.ModelViewSet):
    queryset  = Product.objects.all()
    serializer_class  = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
