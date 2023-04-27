from rest_framework import serializers

from accounts.models import *
from orders.models import *


# SubcategorySerializer
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['subcatgName']


# Category Serializer
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
        fields = ['id', 'item', 'price', 'quantity', 'category', 'subCategory', 'product', 'image']


# Lsit accounts
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = customerUser
        fields = ['username', 'email']


# productSerializer Item Only
class CartproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('item', 'price', 'image',)


# cart items Serializer
class CartItemSerializer(serializers.ModelSerializer):
    product = CartproductSerializer(many=False)
    itemtotal = serializers.SerializerMethodField(method_name="total")

    class Meta:
        model = CartItems
        fields = ['id', 'product', 'quantity', 'itemtotal']

    def total(self, cartitems: CartItems):
        return cartitems.quantity * cartitems.product.price


# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    GrandTotal = serializers.SerializerMethodField(method_name='main_total')
    class Meta:
        model = Cart
        fields = ['id', 'items', "GrandTotal"]

    def main_total(self, cart:Cart):
        items = cart.items.all()
        sum =0
        for item in items:
            sum += item.quantity*item.product.price
        return sum

