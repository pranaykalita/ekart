from django.urls import path, include
from .views import *

urlpatterns = [
    # http://127.0.0.1:8000/api/products/
    path('products/', ProductApiview.as_view()),

    # http://127.0.0.1:8000/api/products/18
    path('products/<int:id>/', ProductsRetriveApiview.as_view()),

    # http://127.0.0.1:8000/api/products/category/?categoryName=T-shirt
    path('products/category/', ProductbyCategoryApiview.as_view(),name="product_by_category"),

    # http://127.0.0.1:8000/api/products/subcategory/?subcatgName=T-shirt
    path('products/subcategory/', ProductbyCategoryApiview.as_view(),name="product_by_subcategory"),

    # http://127.0.0.1:8000/api/category/
    path('category/', CategoryApiview.as_view(), name="category_filter"),



    ]