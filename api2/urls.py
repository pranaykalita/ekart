from django.urls import path
from .views import *

urlpatterns = [
    # products List and By category And subcategory Also
    # http://127.0.0.1:8000/api2/products/view/?cat=Fashion
    path('products/', ProductListWithCategoryView.as_view()),

    # single product Retrive
    # http://127.0.0.1:8000/api2/product/item/1/
    path('product/item/<int:id>/', ProductRetriveView.as_view()),
    
    # category
    # http://127.0.0.1:8000/api2/categorylist/
    path('categorylist/', CategorySubcategoryView.as_view()),

    # User account
    # http://127.0.0.1:8000/api2/accounts/
    path('accounts/', UserAccountView.as_view()),

    # cart View
    path('cart/', cartView.as_view(),)
]
