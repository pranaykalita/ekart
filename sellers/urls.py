from django.urls import path
from .views import *

urlpatterns = [

    # seller Dashbaord
    path('', dashboard, name="dashboard"),
    path('dashboard/', dashboard, name="dashboard"),
    # category
    path('category/', category, name="category"),
    # category Views
    path('addcategory/', addCategory, name="addcategory"),
    path('deletecategory/', deleteCategory, name="deletecategory"),
    path('updatecategory/<str:id>', updateCategory, name="updateCategory"),
    # subcategory Views
    path('addsubcategory/',addSubCategory, name="addsubcategory"),
    path('deletesubcategory/', deleteSubCategory, name="deletesubcategory"),
    path('updatesubcategory/<str:id>', updatesubCategory, name="updatesubCategory"),

    # products
    path('products/', product,name="products"),
    path('addproducts/', Addproduct, name="addproducts"),
    path('deleteprod/<int:id>/', deleteproduct, name="deleteproduct"),
    path('updateproduct/<int:id>/', updateproduct, name="updateproduct"),



]
