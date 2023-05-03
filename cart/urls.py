from django.urls import path
from .views import *

urlpatterns = [
    path('', cartpage, name="cartpage"),

    path('delete/<int:item_id>', deletecartItem, name="itmdeletecart"),

    path('deletecart/', deltecart, name="deltecart"),

    path('addtocart/<int:prod_id>', addtocart, name="additmtocart"),


]
