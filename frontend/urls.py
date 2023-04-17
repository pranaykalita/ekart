from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage),
    path('product/item/<str:id>/', product),



]
