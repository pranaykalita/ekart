from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from products.models import *
from accounts.models import customerUser


# #######################
# Multiple LookUP field Custom Mixin
class MultipleFieldLookupORMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base.html queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            try:                                  # Get the result with one or more fields.
                filter[field] = self.kwargs[field]
            except Exception:
                pass
        return get_object_or_404(queryset, **filter)  # Lookup the object
# #######################


# List all Username And Emails
class UserAccountView(ListModelMixin,GenericAPIView):
    queryset = customerUser.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# List Category With Subcategory
class CategorySubcategoryView(ListModelMixin,GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySubcategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# List All Products
class ProductListWithCategoryView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__categoryName', 'subCategory__subcatgName']

    def get_queryset(self):
        category = self.request.query_params.get('cat', None)
        if category:
            search = Q(category__categoryName=category) | Q(subCategory__subcatgName=category)
            queryset = Product.objects.filter(search).all()
        else:
            queryset = Product.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# List Single Products
class ProductRetriveView(RetrieveModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# cart lsit All items and Create If Not present
class cartCreateLsitallView(ListModelMixin,CreateModelMixin, GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(customeruser=self.request.user)

# cart Single View
class cartRetriveView(RetrieveModelMixin,MultipleFieldLookupORMixin, GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDataSerializer
    lookup_field = lookup_fields = ('id', 'customeruser')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

