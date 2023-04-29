from django.urls import path,include
from .views import *

urlpatterns = [

    # seller Dashbaord
    path('', dashboard, name="sellerdashboard"),
    path('dashboard/', dashboard, name="sellerdashboard"),
    # category
    path('category/', category, name="sellercategory"),

    # orders
    path('orders/', orders, name="sellerorders"),
    # invoice
    path('invoice/', invoice, name="sellerinvoice"),
    # messages
    path('Messages/', Messages, name="sellermessages"),

    # category CRUD
    path('addcategory/', addCategory, name="selleraddcategory"),
    path('deletecategory/', deleteCategory, name="sellerdeletecategory"),
    path('updatecategory/<str:id>', updateCategory, name="sellerupdateCategory"),

    # subcategory CRUD
    path('addsubcategory/',addSubCategory, name="selleraddsubcategory"),
    path('deletesubcategory/', deleteSubCategory, name="sellerdeletesubcategory"),
    path('updatesubcategory/<str:id>', updatesubCategory, name="sellerupdatesubCategory"),

    # products
    path('products/', product, name="sellerproducts"),
    path('addproducts/', Addproduct, name="selleraddproducts"),
    path('deleteprod/<int:id>/', deleteproduct, name="sellerdeleteproduct"),
    path('updateproduct/<int:id>/', updateproduct, name="sellerupdateproduct"),



]
