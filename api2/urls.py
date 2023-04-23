from django.urls import path
from .views import *

urlpatterns = [
    # products
    path('products/', ProductView.as_view()),

    # single product Retrive
    path('product/item/<int:id>/', ProductRetriveView.as_view()),

    # product show by category or Subcategory
    path('product/item/', ProductByCategoryLimitView.as_view()),

    # category
    path('categorylist/', CategorySubcategoryView.as_view()),

    # User account
    path('accounts/', UserAccountView.as_view()),
]
