from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/', ProductApiview.as_view()),
    path('products/<int:id>/', ProductsRetriveApiview.as_view()),

    path('category/', CategoryApiview.as_view()),




    ]