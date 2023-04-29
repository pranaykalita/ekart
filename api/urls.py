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

    # cart View and Create Cart
    path('cart/', cartCreateLsitallView.as_view()),

    # Cart Item Display by userid and cartid
    path('cart/<int:customeruser>/<str:id>', cartRetriveView.as_view()),

]
