from django.urls import path
from .views import *

urlpatterns = [
    # products
    path('products/', ProductView.as_view()),
    path('product/item/<int:id>/', ProductRetriveView.as_view()),

    # category
    path('categorylist/',CategorySubcategoryView.as_view()),

    # User account
    path('accounts/', UserAccountView.as_view()),
]
