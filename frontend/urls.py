from django.urls import path
from .views import *
from accounts.views import *

urlpatterns = [

    path('', homepageView,name="frontendhome"),
    path('product/item/<str:id>/', singleproductView,name="frontendprodutsingle"),

    path('products/', productsView,name="frontendproducts"),

]
