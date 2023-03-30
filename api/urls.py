from django.urls import path
from .views import *

urlpatterns = [
    # seller Dashbaord
    # path('products/', productApiView.as_view()),
    path('products/', productApiView.as_view(), name="productApi"),
    path('productdata/', productDataApiView.as_view(),name="productDataApi" ),
    path('category/', CategoryApiView.as_view(),name="categoryApi" ),
    path('subcategory/', SubCategoryApiView.as_view(),name="subcategoryApi" ),

]
